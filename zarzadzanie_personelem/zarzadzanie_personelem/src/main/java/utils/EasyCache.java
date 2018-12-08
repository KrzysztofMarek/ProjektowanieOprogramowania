
package utils;

import com.google.gson.Gson;
import com.google.gson.reflect.TypeToken;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.Set;

public class EasyCache{
    
    private static Set cache = new HashSet();
    
    public static <T> void addElement (T value){
        cache.add(value);
    }
    
    public static Integer getSize(){
        return cache.size();
    }

    public static Set getAllElements(){
        return cache;
    }    

    public static <T> void addJsonArray(String arrayJson, Class T) {
        cache.clear();
        
        ArrayList<T> array = (new Gson()).fromJson(
                arrayJson,
                new TypeToken<ArrayList<T>>(){}.getType()
        );
        
        cache.addAll(array);
    }
}
