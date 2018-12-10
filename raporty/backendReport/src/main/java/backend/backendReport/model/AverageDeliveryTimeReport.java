package backend.backendReport.model;

import java.util.List;

/**
 * Created by Piotr on 2018-12-10.
 */
public class AverageDeliveryTimeReport {

    private List<AverageDeliveryTimeNode> nodes;

    public List<AverageDeliveryTimeNode> getNodes() {
        return nodes;
    }

    public void setNodes(List<AverageDeliveryTimeNode> nodes) {
        this.nodes = nodes;
    }
}
