# utility library to keep main notebook or python file clean
# for each class or function, write detailed docstring for readability

import plotly.express as px
import pandas as pd

def plot_ts_open_hatch(dfi=None, fac_id=None, fac_name=None, t_drone_open_hatch=None, plot_dir=None):
    """ 
    plotting function to plot time series of one single facility
    dfi: pd.DataFrame with two columns, one is timestamp, one is pressure_osi
    t_drone_open_hatch: datetime or string in a format that could be converted to datetime
    fac_id: facility id
    fac_name: facility name
    plot_dir: directory to save the figure
    """
    assert isinstance(dfi, pd.DataFrame)
    assert 'timestamp' in dfi
    assert 'pressure_osi' in dfi

            
    fig = px.scatter(dfi, x='timestamp', y='pressure_osi')

    if t_drone_open_hatch is not None:
        assert pd.to_datetime(t_drone_open_hatch), 'needs to in a format convertable to datetime'
        t_drone_open_hatch = pd.to_datetime(t_drone_open_hatch)
        fig.add_traces(px.line(x=[t_drone_open_hatch, t_drone_open_hatch], y=[dfi.pressure_osi.min(), dfi.pressure_osi.max()], color_discrete_sequence=['red']).data)

    fig.update_layout(height=900, width=1600, title=f'Facility ID: {fac_id}, {fac_name}, hatch open: {t_drone_open_hatch}', xaxis_title='DateTime', yaxis_title='Pressure, OSI', font=dict(size=18))

    if plot_dir is not None: fig.write_image(f'{plot_dir}/{fac_id}-[{fac_name}].png', engine='orca')
    
    return fig