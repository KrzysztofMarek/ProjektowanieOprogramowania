package ExternalServices;

import Models.*;
import Tools.*;

import java.io.IOException;
import java.io.InputStream;
import java.io.StringWriter;
import java.io.UnsupportedEncodingException;
import java.util.ArrayList;
import java.util.List;

import org.apache.http.HttpEntity;
import org.apache.http.HttpResponse;
import org.apache.http.NameValuePair;
import org.apache.http.client.ClientProtocolException;
import org.apache.http.client.HttpClient;
import org.apache.http.client.entity.UrlEncodedFormEntity;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.entity.ContentType;
import org.apache.http.entity.StringEntity;
import org.apache.http.impl.client.HttpClients;
import org.apache.http.message.BasicNameValuePair;
import org.apache.tomcat.util.http.fileupload.IOUtils;
import org.json.JSONArray;
import org.json.JSONObject;



public class DbService {

    private String componentUrl;

    public DbService(){
        this.componentUrl = ""; 
    }

    public Integer AddOrder(int clientId, int restaurantId, ArrayList<OrderItem> products, double price)
            throws UnsupportedOperationException, IOException {
        HttpClient httpclient = HttpClients.createDefault();
        HttpPost httppost = new HttpPost(componentUrl);

        JSONObject json = new JSONObject();
        json.put("id_klienta", clientId);
        json.put("id_restauracji", restaurantId);
        json.put("kwota", price);
        
        JSONArray array = new JSONArray();
        for (OrderItem orderItem : products) {
            JSONObject item = new JSONObject();
            item.put("id_dania", orderItem.id_dania);
            item.put("nazwa", orderItem.nazwa);
            array.put(item);
        }
        json.put("lista", array);

        StringEntity requestEntity = new StringEntity(
            json.toString(),
            ContentType.APPLICATION_JSON);

        httppost.setEntity(requestEntity);

        //Execute and get the response.
        HttpResponse response = httpclient.execute(httppost);
        HttpEntity entity = response.getEntity();

        if (entity != null) {
            try (InputStream instream = entity.getContent()) {
                return Integer.parseInt(StringTools.convertStreamToString(instream));
            }
        }
        return null;
    }

    public boolean EditOrder(int orderId, ArrayList<Product> products, double price){
        return false;
    }

    public boolean ChangeOrderStatus(int orderId, String status){
        return false;
    }

    public boolean RateOrder(int orderId, int rating){
        return false;
    }

    public ArrayList<Integer> GetPreviousOrdersIds(int clientId){
        ArrayList<Integer> ordersIds = new ArrayList<Integer>();
        ordersIds.add(124412);

        return ordersIds;
    }

    public Order GetOrder(int orderId){
        return new Order();
    }
}