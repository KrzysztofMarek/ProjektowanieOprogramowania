package platnosci.Entity;

import org.junit.Test;
import static org.junit.Assert.*;

public class PaymentVerifierTest {
        
    @Test
    public void testProcessInvalid() {
        String paymentFormJson = "{\n" +
                            "    \"id_klienta\": \"1\",\n" +
                            "    \"id_zamowienia\": \"1\",\n" +
                            "    \"sposób_zapłaty\": \"cos\"\n" +
                            "  }";
        PaymentVerifier paymentVerifier = new PaymentVerifier();
        String result = paymentVerifier.process(paymentFormJson, null);
        assertEquals(result, "Invalid input");
    }
    
}
