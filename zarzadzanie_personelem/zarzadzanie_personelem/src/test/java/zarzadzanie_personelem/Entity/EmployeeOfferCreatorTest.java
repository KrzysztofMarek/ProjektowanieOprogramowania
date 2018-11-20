package zarzadzanie_personelem.Entity;

import com.google.gson.Gson;
import org.junit.Test;
import static org.junit.Assert.*;
import org.junit.runner.RunWith;import org.mockito.Mockito;
import org.powermock.api.mockito.PowerMockito;
import org.powermock.core.classloader.annotations.PrepareForTest;
import org.powermock.modules.junit4.PowerMockRunner;

@RunWith(PowerMockRunner.class)
@PrepareForTest(EmployeeOfferCreator.class)
public class EmployeeOfferCreatorTest {
    
    String invalidInput = new Gson().toJson("Invalid input");
    
    @Test
    public void testCreateEmployeeOfferCorrect() throws Exception{
        String result;
        String employeeOfferFormJson;
        
        employeeOfferFormJson = "{\n" +
                                "    \"id_restauracji\": \"1\", \n" +
                                "    \"etat\": \"40\",\n" +
                                "    \"telefon\": \"123 123 123\",\n" +
                                "    \"stanowisko\": \"Kucharz\"\n"+
                                " } ";
        
        result =helperValidator(employeeOfferFormJson);
        assertNotEquals(result, invalidInput);   
    }    
       
    @Test
    public void testCreateEmployeeOfferIncorrect() throws Exception{
        String result;
        String employeeOfferFormJson;
        
        employeeOfferFormJson = "{\n" +
                                "    \"id_restauracji\": \"1\", \n" +
                                "    \"etat\": \"40\",\n" +
                                "    \"telefon\": \"123 123\",\n" +
                                "    \"stanowisko\": \"Kucharz\"\n"+
                                " } ";
        
        result =helperValidator(employeeOfferFormJson);
        assertEquals(result, invalidInput);   
    }    
    
    private String helperValidator(String formJson) throws Exception{
        EmployeeOfferCreator employeeOfferCreator = new EmployeeOfferCreator();
        EmployeeOfferCreator employeeOfferCreatorSpy = PowerMockito.spy(employeeOfferCreator);
        
        PowerMockito.doReturn("Success").when(employeeOfferCreatorSpy, "saveEmployeeOfferToDB", Mockito.any(), Mockito.any());
        PowerMockito.doNothing().when(employeeOfferCreatorSpy, "saveEmployeeOfferToCache", Mockito.any());
        String result = employeeOfferCreatorSpy.createEmployeeOffer(formJson, "");
        return result;
    }
    
}
