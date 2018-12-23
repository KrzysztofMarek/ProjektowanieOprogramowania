/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package zarzadzanie_siecia.Entity;

import com.google.gson.Gson;
import org.junit.Test;
import static org.junit.Assert.*;
import org.junit.runner.RunWith;
import org.mockito.Mockito;
import org.powermock.api.mockito.PowerMockito;
import org.powermock.core.classloader.annotations.PrepareForTest;
import org.powermock.modules.junit4.PowerMockRunner;


@RunWith(PowerMockRunner.class)
@PrepareForTest(RestaurantCreator.class)
public class RestaurantCreatorTest {
    
    String invalidInput = new Gson().toJson("Invalid input");

     @Test
    public void testCreateRestaurantCorrect() throws Exception{
        String result;
        String restaurantFormJson;
        
        restaurantFormJson = "{\n" +
                                "    \"nazwa\": \"Amrit\", \n" +
                                "    \"adres\": \"40\" \n" +
                                " } ";
        
        result =helperValidator(restaurantFormJson);
        assertNotEquals(result, invalidInput);   
    }    
       
    @Test
    public void testCreateRestaurantNameLongerThan30Signs() throws Exception{
        String result;
        String restaurantFormJson;
        
        restaurantFormJson = "{\n" +
                                "    \"nazwa\": \"Aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\", \n" +
                                "    \"adres\": \"40\" \n" +
                                " } ";
        
        result =helperValidator(restaurantFormJson);
        assertEquals(result, invalidInput);   
    }    
       
    @Test
    public void testCreateRestaurantNameIllegalSigns() throws Exception{
        String result;
        String restaurantFormJson;
        
        restaurantFormJson = "{\n" +
                                "    \"nazwa\": \"Ąę\", \n" +
                                "    \"adres\": \"40\" \n" +
                                " } ";
        
        result =helperValidator(restaurantFormJson);
        assertEquals(result, invalidInput);   
    }    
       
    @Test
    public void testCreateRestaurantNameFirstLetterNotUppercase() throws Exception{
        String result;
        String restaurantFormJson;
        
        restaurantFormJson = "{\n" +
                                "    \"nazwa\": \"amrit\", \n" +
                                "    \"adres\": \"40\" \n" +
                                " } ";
        
        result =helperValidator(restaurantFormJson);
        assertEquals(result, invalidInput);   
    }    
    
    private String helperValidator(String formJson) throws Exception{
        RestaurantCreator restaurantCreator = new RestaurantCreator();
        RestaurantCreator restaurantCreatorSpy = PowerMockito.spy(restaurantCreator);
        
        PowerMockito.doReturn("Success").when(restaurantCreatorSpy, "saveRestaurantToDB", Mockito.any(), Mockito.any());
        String result = restaurantCreatorSpy.createRestaurant(formJson, "");
        return result;
    }
    
}
