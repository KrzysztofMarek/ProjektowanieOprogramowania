package backend.backendReport.model;

import java.util.List;

/**
 * Created by Piotr on 2018-11-19.
 */
public class CompletedOrderReport {

    private List<CompletedOrderNode> nodes;

    public List<CompletedOrderNode> getNodes() {
        return nodes;
    }

    public void setNodes(List<CompletedOrderNode> nodes) {
        this.nodes = nodes;
    }
}
