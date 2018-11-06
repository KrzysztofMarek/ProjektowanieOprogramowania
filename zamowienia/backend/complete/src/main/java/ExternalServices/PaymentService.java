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



public class PaymentService {

    private String componentUrl;

    public PaymentService(){
        this.componentUrl = "";
    }

    public String PayForOrder(int orderId, int clientId, double price, int pointsUsed)
            throws UnsupportedOperationException, IOException {
        HttpClient httpclient = HttpClients.createDefault();
        HttpPost httppost = new HttpPost(componentUrl);

        JSONObject json = new JSONObject();
        json.put("id_zamowienia", orderId);
        json.put("id_klienta", clientId);
        json.put("kwota", price);
        json.put("wykorzystane_punkty", pointsUsed);

        StringEntity requestEntity = new StringEntity(
            json.toString(),
            ContentType.APPLICATION_JSON);

        httppost.setEntity(requestEntity);

        //Execute and get the response.
        HttpResponse response = httpclient.execute(httppost);
        HttpEntity entity = response.getEntity();

        if (entity != null) {
            try (InputStream instream = entity.getContent()) {
                return StringTools.convertStreamToString(instream);
            }
        }
        return null;
    }
}