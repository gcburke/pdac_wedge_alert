from __future__ import annotations

import logging

from pdac_alert_wedge.analysis.cost import default_cost_parameters, icer
from pdac_alert_wedge.analysis.pathway import Lever, ReachState, effective_reach, rank_levers
from pdac_alert_wedge.analysis.wedge import analyze_wedge, subgroup_table
from pdac_alert_wedge.data.simulate import compact_bundle

logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger("pdac_alert_wedge.audit")

def main() -> None:
    bundle = compact_bundle(n=512)
    wedge = analyze_wedge(bundle.deployment)
    state = ReachState(sensitivity=0.384, adoption=0.623, completion=0.783, kappa=1.0)
    levers = rank_levers(state, [Lever("sensitivity", 0.384, 0.40, 9.0), Lever("adoption", 0.623, 0.85, 2.0), Lever("completion", 0.783, 0.90, 3.0)])
    cost = icer("NOD", 100000, 0.0172, 2847, 1389, default_cost_parameters(), 0.71)
    subgroups = subgroup_table(bundle.deployment, "platform")
    LOGGER.info("or %.6f reach %.6f lever %s icer %.2f subgroups %s", wedge.primary.estimate, effective_reach(state.sensitivity, state.adoption, state.completion), levers[0].name, cost.icer, len(subgroups))

if __name__ == "__main__":
    main()
