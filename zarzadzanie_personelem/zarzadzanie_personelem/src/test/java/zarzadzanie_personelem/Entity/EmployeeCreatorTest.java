package zarzadzanie_personelem.Entity;

import com.google.gson.Gson;
import org.junit.Test;
import static org.junit.Assert.*;
import org.junit.runner.RunWith;import org.mockito.Mockito;
import org.powermock.api.mockito.PowerMockito;
import org.powermock.core.classloader.annotations.PrepareForTest;
import org.powermock.modules.junit4.PowerMockRunner;

@RunWith(PowerMockRunner.class)
@PrepareForTest(EmployeeCreator.class)
public class EmployeeCreatorTest {
    
    String invalidInput = new Gson().toJson("Invalid input");
    
    @Test
    public void testCreateEmployeeNameCorrect() throws Exception{
        String result;
        String employeeFormJson;
        
        employeeFormJson = "{\n" +
                                "    \"id_restauracji\": \"1\", \n" +
                                "    \"imie\": \"Adrian\",\n" +
                                "    \"nazwisko\": \"Hasz\",\n" +
                                "    \"telefon\": \"123456789\",\n" +
                                "    \"stanowisko\": \"Kucharz\",\n" +
                                "    \"id_pracownika\": \"haszImasz\",\n" +
                                "    \"haslo\": \"Pyth0n_3xp3rt!\"\n" +
                                " } ";
        
        result =helperValidator(employeeFormJson);
        assertNotEquals(result, invalidInput);   
    }    
        
    @Test
    public void testCreateEmployeeNameFirstLetterUpperCase() throws Exception{
        String result;
        String employeeFormJson;
        
        employeeFormJson = "{\n" +
                                "    \"id_restauracji\": \"1\", \n" +
                                "    \"imie\": \"adam\",\n" +
                                "    \"nazwisko\": \"Adam\",\n" +
                                "    \"telefon\": \"1\",\n" +
                                "    \"stanowisko\": \"a\",\n" +
                                "    \"id_pracownika\": \"a\",\n" +
                                "    \"haslo\": \"a\"\n" +
                                " } ";
        
        result =helperValidator(employeeFormJson);
        assertEquals(result, invalidInput);
    }
    
    @Test
    public void testCreateEmployeeNameOnlyLetters() throws Exception{
        String result;
        String employeeFormJson;
        
        employeeFormJson = "{\n" +
                                "    \"id_restauracji\": \"1\", \n" +
                                "    \"imie\": \"Adam99\",\n" +
                                "    \"nazwisko\": \"Adam\",\n" +
                                "    \"telefon\": \"1\",\n" +
                                "    \"stanowisko\": \"a\",\n" +
                                "    \"id_pracownika\": \"a\",\n" +
                                "    \"haslo\": \"a\"\n" +
                                " } ";
        
        result =helperValidator(employeeFormJson);
        assertEquals(result, invalidInput);
        
        employeeFormJson = "{\n" +
                                "    \"id_restauracji\": \"1\", \n" +
                                "    \"imie\": \"Adam!\",\n" +
                                "    \"nazwisko\": \"Adam\",\n" +
                                "    \"telefon\": \"1\",\n" +
                                "    \"stanowisko\": \"a\",\n" +
                                "    \"id_pracownika\": \"a\",\n" +
                                "    \"haslo\": \"a\"\n" +
                                " } ";
        
        result =helperValidator(employeeFormJson);
        assertEquals(result, invalidInput);
        
        employeeFormJson = "{\n" +
                                "    \"id_restauracji\": \"1\", \n" +
                                "    \"imie\": \"Adam adam\",\n" +
                                "    \"nazwisko\": \"Adam\",\n" +
                                "    \"telefon\": \"1\",\n" +
                                "    \"stanowisko\": \"a\",\n" +
                                "    \"id_pracownika\": \"a\",\n" +
                                "    \"haslo\": \"a\"\n" +
                                " } ";
        
        result =helperValidator(employeeFormJson);
        assertEquals(result, invalidInput);
    }
    
    @Test
    public void testCreateEmployeeNameMax20Letters() throws Exception{
        String result;
        String employeeFormJson;
        
        
        employeeFormJson = "{\n" +
                                "    \"id_restauracji\": \"1\", \n" +
                                "    \"imie\": \"Adamadamadamadamadamadamadamadam\",\n" +
                                "    \"nazwisko\": \"Adam\",\n" +
                                "    \"telefon\": \"1\",\n" +
                                "    \"stanowisko\": \"a\",\n" +
                                "    \"id_pracownika\": \"a\",\n" +
                                "    \"haslo\": \"a\"\n" +
                                " } ";
        
        result =helperValidator(employeeFormJson);
        assertEquals(result, invalidInput);
        
    }
    
    @Test
    public void testCreateEmployeeLastNameOnlyLetters() throws Exception{
        String result;
        String employeeFormJson;        
        
        employeeFormJson = "{\n" +
                                "    \"id_restauracji\": \"1\", \n" +
                                "    \"imie\": \"Adam\",\n" +
                                "    \"nazwisko\": \"Adam99\",\n" +
                                "    \"telefon\": \"1\",\n" +
                                "    \"stanowisko\": \"a\",\n" +
                                "    \"id_pracownika\": \"a\",\n" +
                                "    \"haslo\": \"a\"\n" +
                                " } ";
        
        result =helperValidator(employeeFormJson);
        assertEquals(result, invalidInput);        
        
        employeeFormJson = "{\n" +
                                "    \"id_restauracji\": \"1\", \n" +
                                "    \"imie\": \"Adam\",\n" +
                                "    \"nazwisko\": \"Adam!\",\n" +
                                "    \"telefon\": \"1\",\n" +
                                "    \"stanowisko\": \"a\",\n" +
                                "    \"id_pracownika\": \"a\",\n" +
                                "    \"haslo\": \"a\"\n" +
                                " } ";
        
        result =helperValidator(employeeFormJson);
        assertEquals(result, invalidInput);        
        
        employeeFormJson = "{\n" +
                                "    \"id_restauracji\": \"1\", \n" +
                                "    \"imie\": \"Adam\",\n" +
                                "    \"nazwisko\": \"Adam adam\",\n" +
                                "    \"telefon\": \"1\",\n" +
                                "    \"stanowisko\": \"a\",\n" +
                                "    \"id_pracownika\": \"a\",\n" +
                                "    \"haslo\": \"a\"\n" +
                                " } ";
        
        result =helperValidator(employeeFormJson);
        assertEquals(result, invalidInput);
        
    }
    
    @Test
    public void testCreateEmployeeNameMax30Letters() throws Exception{
        String result;
        String employeeFormJson;
        
        
        employeeFormJson = "{\n" +
                                "    \"id_restauracji\": \"1\", \n" +
                                "    \"imie\": \"AdamadamadamadamadamadamadamadamAdamadamadamadamadamadamadamadam\",\n" +
                                "    \"nazwisko\": \"Adam\",\n" +
                                "    \"telefon\": \"1\",\n" +
                                "    \"stanowisko\": \"a\",\n" +
                                "    \"id_pracownika\": \"a\",\n" +
                                "    \"haslo\": \"a\"\n" +
                                " } ";
        
        result =helperValidator(employeeFormJson);
        assertEquals(result, invalidInput);
        
    }
        
    @Test
    public void testCreateEmployeeTelephoneOnlyPhoneSigns() throws Exception{
        String result;
        String employeeFormJson;
        
        employeeFormJson = "{\n" +
                                "    \"id_restauracji\": \"1\", \n" +
                                "    \"imie\": \"Adam\",\n" +
                                "    \"nazwisko\": \"Adam\",\n" +
                                "    \"telefon\": \"123abc123\",\n" +
                                "    \"stanowisko\": \"a\",\n" +
                                "    \"id_pracownika\": \"a\",\n" +
                                "    \"haslo\": \"a\"\n" +
                                " } ";
        
        result =helperValidator(employeeFormJson);
        assertEquals(result, invalidInput);
    }
        
    @Test
    public void testCreateEmployeeTelephoneOnly9or11or13Signs() throws Exception{
        String result;
        String employeeFormJson;
        
        employeeFormJson = "{\n" +
                                "    \"id_restauracji\": \"1\", \n" +
                                "    \"imie\": \"Adam\",\n" +
                                "    \"nazwisko\": \"Adam\",\n" +
                                "    \"telefon\": \"123 123 123 123\",\n" +
                                "    \"stanowisko\": \"a\",\n" +
                                "    \"id_pracownika\": \"a\",\n" +
                                "    \"haslo\": \"a\"\n" +
                                " } ";
        
        result =helperValidator(employeeFormJson);
        assertEquals(result, invalidInput);
    }
        
    @Test
    public void testCreateEmployeeTelephoneWithPlusOnly11Signs() throws Exception{
        String result;
        String employeeFormJson;
        
        employeeFormJson = "{\n" +
                                "    \"id_restauracji\": \"1\", \n" +
                                "    \"imie\": \"Adam\",\n" +
                                "    \"nazwisko\": \"Adam\",\n" +
                                "    \"telefon\": \"+ 48 123 123 123\",\n" +
                                "    \"stanowisko\": \"a\",\n" +
                                "    \"id_pracownika\": \"a\",\n" +
                                "    \"haslo\": \"a\"\n" +
                                " } ";
        
        result =helperValidator(employeeFormJson);
        assertEquals(result, invalidInput);
    }
        
    @Test
    public void testCreateEmployeeTelephoneCorrect() throws Exception{
        String result;
        String employeeFormJson;
        
        employeeFormJson = "{\n" +
                                "    \"id_restauracji\": \"1\", \n" +
                                "    \"imie\": \"Adam\",\n" +
                                "    \"nazwisko\": \"Adam\",\n" +
                                "    \"telefon\": \"+48123123123\",\n" +
                                "    \"stanowisko\": \"a\",\n" +
                                "    \"id_pracownika\": \"aaaaa\",\n" +
                                "    \"haslo\": \"a\"\n" +
                                " } ";
        
        result =helperValidator(employeeFormJson);
        assertNotEquals(result, invalidInput);
        
        employeeFormJson = "{\n" +
                                "    \"id_restauracji\": \"1\", \n" +
                                "    \"imie\": \"Adam\",\n" +
                                "    \"nazwisko\": \"Adam\",\n" +
                                "    \"telefon\": \"0048123123123\",\n" +
                                "    \"stanowisko\": \"a\",\n" +
                                "    \"id_pracownika\": \"aaaaa\",\n" +
                                "    \"haslo\": \"a\"\n" +
                                " } ";
        
        result =helperValidator(employeeFormJson);
        assertNotEquals(result, invalidInput);
        
        employeeFormJson = "{\n" +
                                "    \"id_restauracji\": \"1\", \n" +
                                "    \"imie\": \"Adam\",\n" +
                                "    \"nazwisko\": \"Adam\",\n" +
                                "    \"telefon\": \"123 123 123\",\n" +
                                "    \"stanowisko\": \"a\",\n" +
                                "    \"id_pracownika\": \"aaaaa\",\n" +
                                "    \"haslo\": \"a\"\n" +
                                " } ";
        
        result =helperValidator(employeeFormJson);
        assertNotEquals(result, invalidInput);
        
        employeeFormJson = "{\n" +
                                "    \"id_restauracji\": \"1\", \n" +
                                "    \"imie\": \"Adam\",\n" +
                                "    \"nazwisko\": \"Adam\",\n" +
                                "    \"telefon\": \"+48 1234 12345\",\n" +
                                "    \"stanowisko\": \"a\",\n" +
                                "    \"id_pracownika\": \"aaaaa\",\n" +
                                "    \"haslo\": \"a\"\n" +
                                " } ";
        
        result =helperValidator(employeeFormJson);
        assertNotEquals(result, invalidInput);
        
        employeeFormJson = "{\n" +
                                "    \"id_restauracji\": \"1\", \n" +
                                "    \"imie\": \"Adam\",\n" +
                                "    \"nazwisko\": \"Adam\",\n" +
                                "    \"telefon\": \"00 48 123456789\",\n" +
                                "    \"stanowisko\": \"a\",\n" +
                                "    \"id_pracownika\": \"aaaaa\",\n" +
                                "    \"haslo\": \"a\"\n" +
                                " } ";
        
        result =helperValidator(employeeFormJson);
        assertNotEquals(result, invalidInput);
    }
        
    @Test
    public void testCreateEmployeeLoginMax20Signs() throws Exception{
        String result;
        String employeeFormJson;
        
        employeeFormJson = "{\n" +
                                "    \"id_restauracji\": \"1\", \n" +
                                "    \"imie\": \"Adam\",\n" +
                                "    \"nazwisko\": \"Adam\",\n" +
                                "    \"telefon\": \"+ 123 123 123\",\n" +
                                "    \"stanowisko\": \"a\",\n" +
                                "    \"id_pracownika\": \"Haslohaslohaslohaslo123\",\n" +
                                "    \"haslo\": \"a\"\n" +
                                " } ";
        
        result =helperValidator(employeeFormJson);
        assertEquals(result, invalidInput);
    }
        
    @Test
    public void testCreateEmployeeLoginMin5Signs() throws Exception{
        String result;
        String employeeFormJson;
        
        employeeFormJson = "{\n" +
                                "    \"id_restauracji\": \"1\", \n" +
                                "    \"imie\": \"Adam\",\n" +
                                "    \"nazwisko\": \"Adam\",\n" +
                                "    \"telefon\": \"+ 123 123 123\",\n" +
                                "    \"stanowisko\": \"a\",\n" +
                                "    \"id_pracownika\": \"Has1\",\n" +
                                "    \"haslo\": \"a\"\n" +
                                " } ";
        
        result =helperValidator(employeeFormJson);
        assertEquals(result, invalidInput);
    }
        
    @Test
    public void testCreateEmployeeLoginNormalSigns() throws Exception{
        String result;
        String employeeFormJson;
        
        employeeFormJson = "{\n" +
                                "    \"id_restauracji\": \"1\", \n" +
                                "    \"imie\": \"Adam\",\n" +
                                "    \"nazwisko\": \"Adam\",\n" +
                                "    \"telefon\": \"+ 123 123 123\",\n" +
                                "    \"stanowisko\": \"a\",\n" +
                                "    \"id_pracownika\": \"ąę\",\n" +
                                "    \"haslo\": \"a\"\n" +
                                " } ";
        
        result =helperValidator(employeeFormJson);
        assertEquals(result, invalidInput);
    }
    
    
    private String helperValidator(String formJson) throws Exception{
        EmployeeCreator employeeCreator = new EmployeeCreator();
        EmployeeCreator employeeCreatorSpy = PowerMockito.spy(employeeCreator);
        
        PowerMockito.doReturn("Success").when(employeeCreatorSpy, "saveEmployeeToDB", Mockito.any(), Mockito.any());
//        PowerMockito.doReturn(new Boolean("True")).when(employeeCreatorSpy, "restaurantExist", Mockito.any(), Mockito.any());
        String result = employeeCreatorSpy.createEmployee(formJson, "", "");
        return result;
    }
    
}
