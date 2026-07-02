"""Dual-pane desktop application for the public productivity demo."""

from __future__ import annotations

from PySide6.QtCore import Qt
from PySide6.QtGui import QBrush, QColor, QFont, QPen
from PySide6.QtWidgets import (
    QAbstractItemView,
    QApplication,
    QFrame,
    QGraphicsRectItem,
    QGraphicsScene,
    QGraphicsTextItem,
    QGraphicsView,
    QHBoxLayout,
    QHeaderView,
    QLabel,
    QMainWindow,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
)

from sample_data import COMPONENTS
from styles import (
    APP_SUBTITLE,
    APP_TITLE,
    CANVAS_BACKGROUND,
    CARD_FILL,
    CARD_OUTLINE,
    MUTED_TEXT_COLOR,
    SELECTED_FILL,
    SELECTED_OUTLINE,
    TEXT_COLOR,
    WINDOW_TITLE,
)


class DualPaneDemo(QMainWindow):
    """Main window for the public dual-pane productivity demo."""

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle(WINDOW_TITLE)
        self.resize(1180, 720)

        self.component_items: dict[str, QGraphicsRectItem] = {}
        self.component_labels: dict[str, QGraphicsTextItem] = {}
        self.selected_component_id: str | None = None

        self.scene = QGraphicsScene(self)
        self.scene.setBackgroundBrush(QBrush(QColor(CANVAS_BACKGROUND)))

        self.diagram_view = QGraphicsView(self.scene)
        self.diagram_view.setRenderHints(self.diagram_view.renderHints())
        self.diagram_view.setMinimumWidth(660)

        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["ID", "Name", "Category", "Status", "Owner"])
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.verticalHeader().setVisible(False)
        self.table.itemSelectionChanged.connect(self._handle_table_selection)

        self.detail_label = QLabel("Select a component in the table to highlight it in the diagram.")
        self.detail_label.setWordWrap(True)
        self.detail_label.setFrameShape(QFrame.StyledPanel)
        self.detail_label.setStyleSheet("padding: 12px; background: #FFFFFF;")

        self.clear_button = QPushButton("Clear Selection")
        self.clear_button.clicked.connect(self.clear_selection)

        self._build_layout()
        self._populate_table()
        self._draw_diagram()

    def _build_layout(self) -> None:
        root = QWidget()
        root_layout = QVBoxLayout(root)
        root_layout.setContentsMargins(18, 18, 18, 18)
        root_layout.setSpacing(14)

        title = QLabel(APP_TITLE)
        title_font = QFont()
        title_font.setPointSize(18)
        title_font.setBold(True)
        title.setFont(title_font)
        title.setStyleSheet(f"color: {TEXT_COLOR};")

        subtitle = QLabel(APP_SUBTITLE)
        subtitle.setStyleSheet(f"color: {MUTED_TEXT_COLOR};")

        header_layout = QVBoxLayout()
        header_layout.addWidget(title)
        header_layout.addWidget(subtitle)
        root_layout.addLayout(header_layout)

        content_layout = QHBoxLayout()
        content_layout.setSpacing(14)

        left_panel = QVBoxLayout()
        left_title = QLabel("Visual technical context")
        left_title.setFont(QFont("Segoe UI", 11, QFont.Bold))
        left_panel.addWidget(left_title)
        left_panel.addWidget(self.diagram_view)

        right_panel_widget = QWidget()
        right_panel_widget.setMinimumWidth(440)
        right_panel = QVBoxLayout(right_panel_widget)
        right_title = QLabel("Structured component data")
        right_title.setFont(QFont("Segoe UI", 11, QFont.Bold))
        right_panel.addWidget(right_title)
        right_panel.addWidget(self.table)
        right_panel.addWidget(QLabel("Selected component details"))
        right_panel.addWidget(self.detail_label)
        right_panel.addWidget(self.clear_button, alignment=Qt.AlignRight)

        content_layout.addLayout(left_panel, stretch=3)
        content_layout.addWidget(right_panel_widget, stretch=2)
        root_layout.addLayout(content_layout)

        self.setCentralWidget(root)

    def _populate_table(self) -> None:
        self.table.setRowCount(len(COMPONENTS))
        for row, component in enumerate(COMPONENTS):
            values = [
                component["id"],
                component["name"],
                component["category"],
                component["status"],
                component["owner"],
            ]
            for column, value in enumerate(values):
                item = QTableWidgetItem(value)
                item.setData(Qt.UserRole, component["id"])
                self.table.setItem(row, column, item)

    def _draw_diagram(self) -> None:
        self.scene.clear()
        self.component_items.clear()
        self.component_labels.clear()

        self.scene.addText("Fictional Technical Assembly Review").setPos(70, 20)

        for component in COMPONENTS:
            x, y, width, height = component["rect"]
            rect_item = QGraphicsRectItem(x, y, width, height)
            rect_item.setBrush(QBrush(QColor(CARD_FILL)))
            rect_item.setPen(QPen(QColor(CARD_OUTLINE), 2))
            self.scene.addItem(rect_item)

            label = QGraphicsTextItem(f"{component['id']}\n{component['name']}")
            label.setDefaultTextColor(QColor(TEXT_COLOR))
            label.setPos(x + 10, y + 10)
            self.scene.addItem(label)

            self.component_items[component["id"]] = rect_item
            self.component_labels[component["id"]] = label

        self._draw_connections()
        self.scene.setSceneRect(0, 0, 720, 380)

    def _draw_connections(self) -> None:
        pen = QPen(QColor("#9CA3AF"), 2)
        self.scene.addLine(270, 125, 270, 125, pen)
        self.scene.addLine(270, 125, 490, 125, pen)
        self.scene.addLine(175, 170, 175, 215, pen)
        self.scene.addLine(572, 175, 512, 240, pen)

    def _handle_table_selection(self) -> None:
        selected_items = self.table.selectedItems()
        if not selected_items:
            return

        component_id = selected_items[0].data(Qt.UserRole)
        self.select_component(component_id)

    def select_component(self, component_id: str) -> None:
        self.selected_component_id = component_id
        for current_id, rect_item in self.component_items.items():
            if current_id == component_id:
                rect_item.setBrush(QBrush(QColor(SELECTED_FILL)))
                rect_item.setPen(QPen(QColor(SELECTED_OUTLINE), 4))
            else:
                rect_item.setBrush(QBrush(QColor(CARD_FILL)))
                rect_item.setPen(QPen(QColor(CARD_OUTLINE), 2))

        component = next(item for item in COMPONENTS if item["id"] == component_id)
        self.detail_label.setText(
            f"<b>{component['id']} - {component['name']}</b><br>"
            f"Category: {component['category']}<br>"
            f"Status: {component['status']}<br>"
            f"Owner: {component['owner']}<br><br>"
            f"{component['notes']}"
        )

    def clear_selection(self) -> None:
        self.table.clearSelection()
        self.selected_component_id = None
        for rect_item in self.component_items.values():
            rect_item.setBrush(QBrush(QColor(CARD_FILL)))
            rect_item.setPen(QPen(QColor(CARD_OUTLINE), 2))
        self.detail_label.setText("Select a component in the table to highlight it in the diagram.")


def run_app() -> None:
    app = QApplication([])
    window = DualPaneDemo()
    window.show()
    app.exec()
