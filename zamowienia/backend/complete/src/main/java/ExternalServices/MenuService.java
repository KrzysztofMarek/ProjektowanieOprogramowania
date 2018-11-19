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
import org.apache.tomcat.util.http.fileupload.IOUtils;
import org.json.JSONArray;
import org.json.JSONObject;



public class MenuService {

    private String componentUrl;
    ArrayList<Product> products = new ArrayList<>();

    public MenuService(){
        this.componentUrl = "http://127.0.0.1:5000/";
    }

    public String getProducts(Integer restaurantId) throws UnsupportedOperationException, IOException, URISyntaxException {
        
        URIBuilder builder = new URIBuilder(this.componentUrl + "pobierz_menu_restauracji");
        builder.setParameter("id_restauracji", restaurantId.toString());

        HttpClient httpclient = HttpClients.createDefault();
        HttpGet request = new HttpGet(builder.build());

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