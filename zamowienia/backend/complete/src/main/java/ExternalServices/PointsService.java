package ExternalServices;

import Models.*;

import java.awt.List;
import java.util.ArrayList;



public class PointsService {

    private String componentUrl;

    public PointsService(){
        this.componentUrl = "";
    }

    public int GetClientPoints(int clientId){
        return 50;
    }
}