from plotly.subplots import make_subplots
import plotly.graph_objects as go


def plot_line(df, columns, title="", secondary_y=None, size=[350, 1000]):
    fig = make_subplots(specs=[[{"secondary_y": True}]]) if secondary_y else go.Figure()

    for i, col in enumerate(columns):
        trace = go.Scatter(
            x=df.index, y=df[col], mode="lines", name=col, line=dict(width=2.0)
        )
        if secondary_y:
            fig.add_trace(trace, secondary_y=secondary_y[i])
        else:
            fig.add_trace(trace)
    fig.update_layout(
        height=size[0],
        width=size[1],
        template="plotly_white",
        title=title,
        margin=dict(l=50, r=80, t=50, b=40),
    )
    fig.show()
