/** @odoo-module **/
import { registry } from "@web/core/registry";
import { Component, useState, onWillStart } from "@odoo/owl";
import { useService } from "@web/core/utils/hooks";

export class RankingBoard extends Component {
    setup() {
        this.orm = useService("orm");
        this.action = useService("action");
        this.state = useState({ players: [] });

        onWillStart(async () => {
            this.state.players = await this.orm.searchRead("mc.player", [], ["name", "tier", "image_url"]);
        });
    }

    openPlayer(id) {
        this.action.doAction({
            type: "ir.actions.act_window",
            res_model: "mc.player",
            res_id: id,
            views: [[false, "form"]],
            target: "new",
        });
    }

    getPlayersByTier(t) {
        return this.state.players.filter(p => p.tier === t);
    }
}
RankingBoard.template = "mc_tiers.RankingBoard";
registry.category("actions").add("mc_ranking_board", RankingBoard);
