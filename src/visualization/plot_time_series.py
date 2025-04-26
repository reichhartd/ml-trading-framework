from plotly.subplots import make_subplots
import plotly.graph_objects as go


def plot_time_series(df, columns, title="", subplot_rows=None):
    size = [350, 1000]

    if subplot_rows and subplot_rows > 1:
        specs = [[{}] for _ in range(subplot_rows)]
        fig = make_subplots(rows=subplot_rows, cols=1, specs=specs)

        cols_per_subplot = max(1, len(columns) // subplot_rows)

        for i, col in enumerate(columns):
            subplot_idx = min(i // cols_per_subplot + 1, subplot_rows)
            trace = go.Scatter(
                x=df.index, y=df[col], mode="lines", name=col, line=dict(width=2.0)
            )

            fig.add_trace(trace, row=subplot_idx, col=1)
    else:
        fig = go.Figure()

        for col in columns:
            trace = go.Scatter(
                x=df.index, y=df[col], mode="lines", name=col, line=dict(width=2.0)
            )
            fig.add_trace(trace)

    height_multiplier = max(1, subplot_rows if subplot_rows else 1)
    fig.update_layout(
        height=size[0] * height_multiplier,
        width=size[1],
        template="plotly_white",
        title=title,
        margin=dict(l=50, r=80, t=50 + 40 * (height_multiplier - 1), b=40),
    )

    fig.show()
