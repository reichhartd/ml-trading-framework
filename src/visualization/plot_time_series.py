from plotly.subplots import make_subplots
import plotly.graph_objects as go


def plot_time_series(df, columns, title="", subplot_rows=1, secondary_y=None, dataset_type=""):
    line_widths = [2] * len(columns)

    if secondary_y is not None:
        specs = [[{"secondary_y": True}] for _ in range(subplot_rows)]
        fig = make_subplots(rows=subplot_rows, specs=specs, shared_xaxes=True)
    else:
        fig = make_subplots(rows=subplot_rows, shared_xaxes=True)

    for idx, column in enumerate(columns):
        row_idx = min(idx + 1, subplot_rows)

        if secondary_y is not None:
            fig.add_trace(
                go.Scatter(
                    x=df.index,
                    y=df[column],
                    mode="lines",
                    name=column,
                    line=dict(width=line_widths[idx]),
                ),
                row=row_idx,
                col=1,
                secondary_y=secondary_y[idx],
            )
        else:
            fig.add_trace(
                go.Scatter(
                    x=df.index,
                    y=df[column],
                    mode="lines",
                    name=column,
                    line=dict(width=line_widths[idx]),
                ),
                row=row_idx,
                col=1,
            )
    fig.update_layout(
        template="plotly_white",
        title=f"{dataset_type} Features - {title}",
        margin=dict(l=50, r=80, t=50, b=40),
        autosize=True,
    )
    fig.show(config={"responsive": True})
