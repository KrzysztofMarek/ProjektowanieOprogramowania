package ExternalServices;

import Models.*;
import Tools.*;

import java.io.IOException;
import java.io.InputStream;
import java.io.StringWriter;
import java.io.UnsupportedEncodingException;
import java.net.URISyntaxException;
import java.util.ArrayList;
import java.util.List;

import org.apache.http.HttpEntity;
import org.apache.http.HttpResponse;
import org.apache.http.NameValuePair;
import org.apache.http.client.ClientProtocolException;
import org.apache.http.client.HttpClient;
import org.apache.http.client.entity.UrlEncodedFormEntity;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.client.utils.URIBuilder;
import org.apache.http.entity.ContentType;
import org.apache.http.entity.StringEntity;
import org.apache.http.impl.client.HttpClients;
import org.apache.http.message.BasicNameValuePair;
import org.apache.http.params.HttpParams;
import org.apache.tomcat.util.http.fileupload.IOUtils;
import org.json.JSONArray;
import org.json.JSONObject;



public class DbService {

    private String componentUrl;

    public DbService(){
        this.componentUrl = "http://127.0.0.1:5000/"; 
    }

    public int GetClientPoints(String clientId) throws ClientProtocolException, IOException, URISyntaxException{
        URIBuilder builder = new URIBuilder(this.componentUrl + "pobierz_punkty_klienta");
        builder.setParameter("id_klienta", clientId);

        HttpClient httpclient = HttpClients.createDefault();
        HttpGet httpGet = new HttpGet(builder.build());

        HttpResponse response = httpclient.execute(httpGet);
        HttpEntity entity = response.getEntity();

        int statusCode = response.getStatusLine().getStatusCode();

        Integer clientPoints;
        try (InputStream instream = entity.getContent()) {
            clientPoints = Integer.parseInt(StringTools.convertStreamToString(instream));
        }

        if(statusCode == 200){
            return clientPoints;
        }

        return 0;
    }

    public boolean AddClientPoints(String clientId, Integer points) throws ClientProtocolException, IOException{
        HttpClient httpclient = HttpClients.createDefault();
        HttpPost httppost = new HttpPost(componentUrl + "dodaj_punkty");

        JSONObject json = new JSONObject();
        json.put("id_klienta", clientId);
        json.put("punkty", points);

        StringEntity requestEntity = new StringEntity(
            json.toString(),
            ContentType.APPLICATION_JSON);

        HttpResponse response = httpclient.execute(httppost);
        HttpEntity entity = response.getEntity();

        int statusCode = response.getStatusLine().getStatusCode();

        if(statusCode == 200){
            return true;
        }

        return false;
    }


    public boolean RemoveClientPoints(String clientId, Integer points) throws ClientProtocolException, IOException{
        HttpClient httpclient = HttpClients.createDefault();
        HttpPost httppost = new HttpPost(componentUrl + "usun_punkty");

        JSONObject json = new JSONObject();
        json.put("id_klienta", clientId);
        json.put("punkty", points);

        StringEntity requestEntity = new StringEntity(
            json.toString(),
            ContentType.APPLICATION_JSON);

        HttpResponse response = httpclient.execute(httppost);
        HttpEntity entity = response.getEntity();

        int statusCode = response.getStatusLine().getStatusCode();

        if(statusCode == 200){
            return true;
        }

        return false;
    }
}