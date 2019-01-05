package ExternalServices;

import Models.*;
import Tools.StringTools;

import java.awt.List;
import java.io.IOException;
import java.io.InputStream;
import java.net.URISyntaxException;
import java.util.ArrayList;

import org.apache.http.HttpEntity;
import org.apache.http.HttpResponse;
import org.apache.http.client.ClientProtocolException;
import org.apache.http.client.HttpClient;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.client.utils.URIBuilder;
import org.apache.http.entity.ContentType;
import org.apache.http.entity.StringEntity;
import org.apache.http.impl.client.HttpClients;
import org.json.JSONObject;



public class PointsService {

    private String componentUrl;

    public PointsService(){
        this.componentUrl = "http://localhost:8091/";
    }

    public int GetClientPoints(String clientId) throws ClientProtocolException, IOException, URISyntaxException{
        URIBuilder builder = new URIBuilder(this.componentUrl + "pobierz_punkty_klienta");
        builder.setParameter("id_klienta", clientId);

        HttpClient httpclient = HttpClients.createDefault();
        HttpGet httpGet = new HttpGet(builder.build());

        HttpResponse response = httpclient.execute(httpGet);
        HttpEntity entity = response.getEntity();

        int statusCode = response.getStatusLine().getStatusCode();

        if(statusCode == 200){
            Integer clientPoints;
            try (InputStream instream = entity.getContent()) {
                clientPoints = Integer.parseInt(StringTools.convertStreamToString(instream));
            }

            return clientPoints;
        }

        return 0;
    }

    public boolean AddClientPoints(String clientId, Integer points) throws ClientProtocolException, IOException, URISyntaxException {
        URIBuilder builder = new URIBuilder(this.componentUrl + "dodaj_punkty");
        builder.setParameter("id_klienta", clientId);
        builder.setParameter("punkty", points.toString());

        HttpClient httpclient = HttpClients.createDefault();
        HttpPost httppost = new HttpPost(builder.build());

        HttpResponse response = httpclient.execute(httppost);
        HttpEntity entity = response.getEntity();

        int statusCode = response.getStatusLine().getStatusCode();

        if(statusCode == 200){
            return true;
        }

        return false;
    }


    public boolean RemoveClientPoints(String clientId, Integer points) throws ClientProtocolException, IOException, URISyntaxException {
        URIBuilder builder = new URIBuilder(this.componentUrl + "usun_punkty");
        builder.setParameter("id_klienta", clientId);
        builder.setParameter("punkty", points.toString());

        HttpClient httpclient = HttpClients.createDefault();
        HttpPost httppost = new HttpPost(builder.build());

        HttpResponse response = httpclient.execute(httppost);
        HttpEntity entity = response.getEntity();

        int statusCode = response.getStatusLine().getStatusCode();

        if(statusCode == 200){
            return true;
        }

        return false;
    }
}