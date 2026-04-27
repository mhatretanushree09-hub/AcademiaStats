# charts.py - functions to create plotly charts
import plotly.express as px
import plotly.graph_objects as go

# common colors used across charts
COLORS = ["#8b5cf6", "#a78bfa", "#6366f1", "#818cf8", "#c4b5fd", "#7c3aed"]
GRADIENT = [[0, "#312e81"], [0.25, "#4c1d95"], [0.5, "#6d28d9"], [0.75, "#8b5cf6"], [1, "#a78bfa"]]

# common dark layout for all charts
LAYOUT = dict(
    paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
    font=dict(family="Inter", color="#cbd5e1"), margin=dict(l=20, r=20, t=40, b=20),
    xaxis=dict(gridcolor="rgba(139,92,246,0.08)"), yaxis=dict(gridcolor="rgba(139,92,246,0.08)"),
)


def bar_chart(df, subjects):
    avg = df[subjects].mean().sort_values()
    fig = px.bar(x=avg.values, y=avg.index, orientation="h", color=avg.values,
                 color_continuous_scale=GRADIENT, labels={"x": "Avg Score", "y": "Subject"})
    fig.update_layout(**LAYOUT, height=350, showlegend=False)
    return fig


def gpa_chart(df, gpa_col, gender_col):
    if gender_col:
        fig = px.violin(df, x=gender_col, y=gpa_col, color=gender_col, box=True,
                        color_discrete_sequence=COLORS)
    else:
        fig = px.histogram(df, x=gpa_col, nbins=20, color_discrete_sequence=COLORS)
    fig.update_layout(**LAYOUT, height=350, showlegend=True)
    return fig


def radar_chart(df, subjects):
    avg = df[subjects].mean()
    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r=avg.values.tolist() + [avg.values[0]],
        theta=avg.index.tolist() + [avg.index[0]],
        fill="toself", fillcolor="rgba(139,92,246,0.15)",
        line=dict(color="#8b5cf6", width=2.5), marker=dict(size=6, color="#a78bfa")
    ))
    fig.update_layout(
        polar=dict(bgcolor="rgba(0,0,0,0)",
                   angularaxis=dict(gridcolor="rgba(139,92,246,0.12)", tickfont=dict(color="#94a3b8")),
                   radialaxis=dict(gridcolor="rgba(139,92,246,0.1)", tickfont=dict(color="#64748b"), range=[0, 100])),
        paper_bgcolor="rgba(0,0,0,0)", font=dict(family="Inter", color="#cbd5e1"),
        height=370, showlegend=False, margin=dict(l=60, r=60, t=40, b=40)
    )
    return fig


def heatmap(df, cols):
    fig = px.imshow(df[cols].corr(), text_auto=".2f", color_continuous_scale=GRADIENT, aspect="auto")
    fig.update_layout(**LAYOUT, height=370)
    fig.update_traces(textfont=dict(color="#e2e8f0", size=11))
    return fig


def scatter_chart(df, att_col, gpa_col, name_col):
    fig = px.scatter(df, x=att_col, y=gpa_col, color=df[gpa_col], size=df[gpa_col],
                     color_continuous_scale=GRADIENT, size_max=14, hover_data=[name_col],
                     labels={att_col: "Attendance (%)", gpa_col: "GPA"}, trendline="ols")
    fig.update_layout(**LAYOUT, height=400, showlegend=False)
    return fig
