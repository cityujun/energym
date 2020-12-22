import datetime
from energym.envs.env_fmu_mod import EnvModFMU

INPUTS_SPECS = {
    "u": {
        "type": "scalar",
        "lower_bound": 0,
        "upper_bound": 1,
        "default": 0,
    }
}

OUTPUTS_SPECS_RAD = {
    "weaBus.HDifHor": {
        "type": "scalar",
        "lower_bound": 0,
        "upper_bound": 1000,
    },
    "weaBus.HDirNor": {
        "type": "scalar",
        "lower_bound": 0,
        "upper_bound": 1000,
    },
    "weaBus.HGloHor": {
        "type": "scalar",
        "lower_bound": 0,
        "upper_bound": 1000,
    },
    "weaBus.HHorIR": {
        "type": "scalar",
        "lower_bound": 0,
        "upper_bound": 1000,
    },
    "sunRad.y": {"type": "scalar", "lower_bound": 0, "upper_bound": 1000},
    "sunHea.Q_flow": {
        "type": "scalar",
        "lower_bound": 0,
        "upper_bound": 100,
    },
    "preHea.Q_flow": {
        "type": "scalar",
        "lower_bound": 0,
        "upper_bound": 100,
    },
    "heaPum.P": {"type": "scalar", "lower_bound": 0, "upper_bound": 100},
    "heaPum.QCon_flow": {
        "type": "scalar",
        "lower_bound": 0,
        "upper_bound": 100,
    },
    "heaPum.QEva_flow": {
        "type": "scalar",
        "lower_bound": 0,
        "upper_bound": 100,
    },
    "heaPum.COP": {"type": "scalar", "lower_bound": 0, "upper_bound": 20},
    "heaPum.COPCar": {
        "type": "scalar",
        "lower_bound": 0,
        "upper_bound": 20,
    },
    "heaPum.TConAct": {
        "type": "scalar",
        "lower_bound": 0,
        "upper_bound": 70,
    },
    "heaPum.TEvaAct": {
        "type": "scalar",
        "lower_bound": 0,
        "upper_bound": 70,
    },
    "rad.Q_flow": {
        "type": "scalar",
        "lower_bound": 0,
        "upper_bound": 100,
    },
    "rad.m_flow": {"type": "scalar", "lower_bound": 0, "upper_bound": 10},
    "temRet.T": {
        "type": "scalar",
        "lower_bound": 273.15,
        "upper_bound": 353.15,
    },
    "temSup.T": {
        "type": "scalar",
        "lower_bound": 273.15,
        "upper_bound": 353.15,
    },
    "TOut.T": {
        "type": "scalar",
        "lower_bound": 253.15,
        "upper_bound": 343.15,
    },
    "temRoo.T": {
        "type": "scalar",
        "lower_bound": 263.15,
        "upper_bound": 343.15,
    },
    "y": {"type": "scalar", "lower_bound": -10, "upper_bound": 70},
}

OUTPUTS_SPECS_SLAB = {
    "weaBus.HDifHor": {
        "type": "scalar",
        "lower_bound": 0,
        "upper_bound": 1000,
    },
    "weaBus.HDirNor": {
        "type": "scalar",
        "lower_bound": 0,
        "upper_bound": 1000,
    },
    "weaBus.HGloHor": {
        "type": "scalar",
        "lower_bound": 0,
        "upper_bound": 1000,
    },
    "weaBus.HHorIR": {
        "type": "scalar",
        "lower_bound": 0,
        "upper_bound": 1000,
    },
    "sunRad.y": {"type": "scalar", "lower_bound": 0, "upper_bound": 1000},
    "sunHea.Q_flow": {
        "type": "scalar",
        "lower_bound": 0,
        "upper_bound": 100,
    },
    "preHea.Q_flow": {
        "type": "scalar",
        "lower_bound": 0,
        "upper_bound": 100,
    },
    "heaPum.P": {"type": "scalar", "lower_bound": 0, "upper_bound": 100},
    "heaPum.QCon_flow": {
        "type": "scalar",
        "lower_bound": 0,
        "upper_bound": 100,
    },
    "heaPum.QEva_flow": {
        "type": "scalar",
        "lower_bound": 0,
        "upper_bound": 100,
    },
    "heaPum.COP": {"type": "scalar", "lower_bound": 0, "upper_bound": 20},
    "heaPum.COPCar": {
        "type": "scalar",
        "lower_bound": 0,
        "upper_bound": 20,
    },
    "heaPum.TConAct": {
        "type": "scalar",
        "lower_bound": 0,
        "upper_bound": 70,
    },
    "heaPum.TEvaAct": {
        "type": "scalar",
        "lower_bound": 0,
        "upper_bound": 70,
    },
    "sla.surf_a.Q_flow": {
        "type": "scalar",
        "lower_bound": 0,
        "upper_bound": 100,
    },
    "sla.surf_b.Q_flow": {
        "type": "scalar",
        "lower_bound": 0,
        "upper_bound": 100,
    },
    "sla.m_flow": {"type": "scalar", "lower_bound": 0, "upper_bound": 10},
    "sla.surf_a.T": {
        "type": "scalar",
        "lower_bound": 273.15,
        "upper_bound": 343.15,
    },
    "sla.surf_b.T": {
        "type": "scalar",
        "lower_bound": 273.15,
        "upper_bound": 343.15,
    },
    "temRet.T": {
        "type": "scalar",
        "lower_bound": 273.15,
        "upper_bound": 353.15,
    },
    "temSup.T": {
        "type": "scalar",
        "lower_bound": 273.15,
        "upper_bound": 353.15,
    },
    "TOut.T": {
        "type": "scalar",
        "lower_bound": 253.15,
        "upper_bound": 343.15,
    },
    "temRoo.T": {
        "type": "scalar",
        "lower_bound": 263.15,
        "upper_bound": 343.15,
    },
    "y": {"type": "scalar", "lower_bound": -10, "upper_bound": 70},
}

default_kpi_options = {
    "kpi1": {"name": "heaPum.P", "type": "avg"},
    "kpi2": {
        "name": "temRoo.T",
        "type": "avg_dev",
        "target": [292.15, 297.15],
    },
    "kpi3": {
        "name": "temRoo.T",
        "type": "tot_viol",
        "target": [292.15, 297.15],
    },
}


class SimpleHouse(EnvModFMU):
    """Containing information for the models SimpleHouseRad-v0 and SimpleHouseSlab-v0

    Subclasses EnvModFMU and inherits its behavior. Simulation based details are
    specified in this class and passed to the constructor of EnvModFMU.
    """

    def __init__(
        self,
        model_path,
        start_day=1,
        start_month=1,
        year=2019,
        simulation_days=21,
        weather="CH_BS_Basel",
        kpi_options=None,
    ):
        """
        Parameters
        ----------
        model_path : str
            Specifies the path to the FMU
        start_day : int, optional
            Day of the month to start the simulation, by default 1
        start_month : int, optional
            Month of the year to start the simulation, by default 1
        year : int, optional
            Year to start the simulation, by default 2019
        simulation_days : int, optional
            Number of days the simulation can run for, by default 10
        weather : str, optional
            Specific weather file to run the simulation, by default
            "CH_ZH_Maur"
        kpi_options : dict, optional
            Dict to specify the tracked KPIs, by default None.
        """
        n_steps = 12
        step_size = 5 * 60
        start_date = datetime.date(year, start_month, start_day)
        delta = start_date - datetime.date(year, 1, 1)
        start_time = delta.total_seconds()
        stop_time = (
            start_time + n_steps * 24 * simulation_days * step_size
        )
        params = {
            "P_nominal": 5e3,
            "COP_nominal": 5.0,
            "therm_cond_G": 500.0,
            "heat_capa_C": 1e7,
            "QRooInt_flow": 700.0,
        }
        init_vals = {"u": 0.0}

        if kpi_options is None:
            kpi_options = default_kpi_options

        if "Rad" in model_path:
            outputs_specs = OUTPUTS_SPECS_RAD
        else:
            outputs_specs = OUTPUTS_SPECS_SLAB
        print(model_path)
        super().__init__(
            model_path,
            start_time,
            stop_time,
            step_size,
            weather,
            INPUTS_SPECS,
            outputs_specs,
            kpi_options,
        )

        self.set_model_variables(
            list(params.keys()), list(params.values())
        )
        self.set_model_variables(
            list(init_vals.keys()), list(init_vals.values())
        )