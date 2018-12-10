package backend.backendReport.model;

import java.util.List;

/**
 * Created by Piotr on 2018-12-10.
 */
public class AverageRealisationTimeReport {

    private List<AverageRealisationTimeNode> nodes;

    public List<AverageRealisationTimeNode> getNodes() {
        return nodes;
    }

    public void setNodes(List<AverageRealisationTimeNode> nodes) {
        this.nodes = nodes;
    }
}
