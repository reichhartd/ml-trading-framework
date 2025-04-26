from plotly.subplots import make_subplots
import plotly.graph_objects as go


def plot_time_series(df, columns, title="", subplot_rows=1):
    lw_id = None
    size = [350, 1000]

    fig = make_subplots(rows=subplot_rows, shared_xaxes=True)
    ii = -1
    for i in columns:
        ii += 1
        fig.add_trace(
            go.Scatter(
                x=df.index,
                y=df[columns[ii]],
                mode="lines",
                name=columns[ii],
                line=dict(width=lw_id[ii]),
            ),
            row=ii + 1,
            col=1,
        )

    fig.update_layout(
        height=size[0],
        width=size[1],
        template="plotly_white",
        title=title,
        margin=dict(l=50, r=80, t=50, b=40),
    )
    fig.show()
