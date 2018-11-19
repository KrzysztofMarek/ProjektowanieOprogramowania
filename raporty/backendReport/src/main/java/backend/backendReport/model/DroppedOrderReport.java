package backend.backendReport.model;

import java.util.List;

/**
 * Created by Piotr on 2018-11-19.
 */
public class DroppedOrderReport {

    private List<DroppedOrderNode> nodes;

    public List<DroppedOrderNode> getNodes() {
        return nodes;
    }

    public void setNodes(List<DroppedOrderNode> nodes) {
        this.nodes = nodes;
    }
}


