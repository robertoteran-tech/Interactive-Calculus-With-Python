"""Small, notebook-friendly helpers shared across course modules."""

from __future__ import annotations

from collections.abc import Callable

import numpy as np
import plotly.graph_objects as go


def configure_plotly() -> None:
    """Set a consistent default renderer when running in Jupyter."""
    import plotly.io as pio

    pio.renderers.default = "jupyterlab"


def sample_function(
    function: Callable[[np.ndarray], np.ndarray],
    start: float = -5,
    stop: float = 5,
    points: int = 500,
    *,
    title: str = "Function",
    x_label: str = "x",
    y_label: str = "f(x)",
) -> go.Figure:
    """Sample a numerical function and return a consistent Plotly figure."""
    x = np.linspace(start, stop, points)
    y = function(x)
    figure = go.Figure(go.Scatter(x=x, y=y, mode="lines", name=y_label))
    figure.update_layout(title=title, xaxis_title=x_label, yaxis_title=y_label)
    figure.update_xaxes(zeroline=True, zerolinecolor="gray")
    figure.update_yaxes(zeroline=True, zerolinecolor="gray")
    return figure
