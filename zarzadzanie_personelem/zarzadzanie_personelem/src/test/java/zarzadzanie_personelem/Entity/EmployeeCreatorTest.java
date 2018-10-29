package zarzadzanie_personelem.Entity;

import org.junit.Test;
import static org.junit.Assert.*;
import org.junit.runner.RunWith;import org.mockito.Mockito;
import org.powermock.api.mockito.PowerMockito;
import org.powermock.core.classloader.annotations.PrepareForTest;
import org.powermock.modules.junit4.PowerMockRunner;

@RunWith(PowerMockRunner.class)
@PrepareForTest(EmployeeCreator.class)
public class EmployeeCreatorTest {
    
    
    @Test
    public void testCreateEmployeeValid() throws Exception{
        String employeeFormJson = "{\n" +
                                "    \"id_restauracji\": \"1\", \n" +
                                "    \"imie\": \"Adam\",\n" +
                                "    \"nazwisko\": \"Adam\",\n" +
                                "    \"telefon\": \"123456789\",\n" +
                                "    \"stanowisko\": \"a\",\n" +
                                "    \"login\": \"a\",\n" +
                                "    \"haslo\": \"a\"\n" +
                                " } ";
        EmployeeCreator employeeCreator = new EmployeeCreator();
        EmployeeCreator employeeCreatorSpy = PowerMockito.spy(employeeCreator);
        
        PowerMockito.doReturn("Success").when(employeeCreatorSpy, "saveEmployeeToDB", Mockito.any());
        String result = employeeCreatorSpy.createEmployee(employeeFormJson, "");
        
        assertEquals(result, "Success");
    }
    
    @Test
    public void testCreateEmployeeInvalid() throws Exception{
        String employeeFormJson = "{\n" +
                                "    \"id_restauracji\": \"1\", \n" +
                                "    \"imie\": \"Adam\",\n" +
                                "    \"nazwisko\": \"Adam\",\n" +
                                "    \"telefon\": \"1\",\n" +
                                "    \"stanowisko\": \"a\",\n" +
                                "    \"login\": \"a\",\n" +
                                "    \"haslo\": \"a\"\n" +
                                " } ";
        EmployeeCreator employeeCreator = new EmployeeCreator();
        EmployeeCreator employeeCreatorSpy = PowerMockito.spy(employeeCreator);
        
        PowerMockito.doReturn("Success").when(employeeCreatorSpy, "saveEmployeeToDB", Mockito.any());
        String result = employeeCreatorSpy.createEmployee(employeeFormJson, "");
        
        assertEquals(result, "Invalid input");
    }
    
}
