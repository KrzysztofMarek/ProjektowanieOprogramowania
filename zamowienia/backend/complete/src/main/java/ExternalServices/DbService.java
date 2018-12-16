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

    public Integer AddOrder(NewOrder newOrder)
            throws UnsupportedOperationException, IOException {
        HttpClient httpclient = HttpClients.createDefault();
        HttpPost httppost = new HttpPost(componentUrl + "dodaj_zamowienie_Z");

        JSONObject json = new JSONObject();
        json.put("id_klienta", newOrder.id_klienta);
        json.put("id_restauracji", newOrder.id_restauracji);
        json.put("kwota", newOrder.kwota);
        json.put("adres", newOrder.adres);
        
        JSONArray array = new JSONArray();
        for (OrderItem orderItem : newOrder.lista_dan) {
            JSONObject item = new JSONObject();
            item.put("id_dania", orderItem.id_dania);
            item.put("nazwa", orderItem.nazwa);
            array.put(item);
        }
        json.put("lista_dan", array);

        StringEntity requestEntity = new StringEntity(
            json.toString(),
            ContentType.APPLICATION_JSON);

        httppost.setEntity(requestEntity);

        //Execute and get the response.
        HttpResponse response = httpclient.execute(httppost);
        HttpEntity entity = response.getEntity();

        int statusCode = response.getStatusLine().getStatusCode();

        if (entity != null) {
            try (InputStream instream = entity.getContent()) {
                return Integer.parseInt(StringTools.convertStreamToString(instream));
            }catch(Exception ex){
                return 0;
            }
        }else{
            if(statusCode == 200){
                return 0;
            }
        }


        return null;
    }

    public boolean EditOrder(int orderId, ArrayList<Product> products, double price){
        return false;
    }

    public boolean ChangeOrderStatus(int orderId, String status) throws URISyntaxException, ClientProtocolException, IOException {
        URIBuilder builder = new URIBuilder(this.componentUrl + "zmien_status_zamowienia_Z");

        HttpClient httpclient = HttpClients.createDefault();
        HttpPost httppost = new HttpPost(builder.build());

        JSONObject json = new JSONObject();
        json.put("id_zamowienia", orderId);
        json.put("status", status);

        StringEntity requestEntity = new StringEntity(
            json.toString(),
            ContentType.APPLICATION_JSON);

        httppost.setEntity(requestEntity);

        HttpResponse response = httpclient.execute(httppost);

        int statusCode = response.getStatusLine().getStatusCode();

        if(statusCode == 200){
            return true;
        }else{
            return false;
        }
    }

    public boolean RateOrder(Integer orderId, String rating) throws URISyntaxException, ClientProtocolException, IOException {
        URIBuilder builder = new URIBuilder(this.componentUrl + "dodaj_ocene_Z");

        HttpClient httpclient = HttpClients.createDefault();
        HttpPost httppost = new HttpPost(builder.build());

        JSONObject json = new JSONObject();
        json.put("id_zamowienia", orderId);
        json.put("ocena", rating);

        StringEntity requestEntity = new StringEntity(
            json.toString(),
            ContentType.APPLICATION_JSON);

        httppost.setEntity(requestEntity);

        HttpResponse response = httpclient.execute(httppost);

        int statusCode = response.getStatusLine().getStatusCode();

        if(statusCode == 200){
            return true;
        }else{
            return false;
        }

    }

    public String GetOrders(Integer userId) throws URISyntaxException, ClientProtocolException, IOException {
        URIBuilder builder = new URIBuilder(this.componentUrl + "pobierz_zamowienia_Z");
        builder.setParameter("id_restauracji", userId.toString());

        HttpClient httpclient = HttpClients.createDefault();
        HttpGet request = new HttpGet(builder.build());

        request.addHeader("Content-Type", "application/json");

        HttpResponse response = httpclient.execute(request);
        HttpEntity entity = response.getEntity();

        
        if (entity != null) {
            try (InputStream instream = entity.getContent()) {
                return StringTools.convertStreamToString(instream);
            }
        }

        return null;
    }
}