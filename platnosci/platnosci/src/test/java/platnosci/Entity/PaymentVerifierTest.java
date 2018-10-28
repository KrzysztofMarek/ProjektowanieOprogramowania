package platnosci.Entity;

import org.junit.Test;
import static org.junit.Assert.*;

public class PaymentVerifierTest {
    
    @Test
    public void testProcessValid() {
        String paymentFormJson = "{\n" +
                            "    \"id_klienta\": \"1\",\n" +
                            "    \"id_zamowienia\": \"1\",\n" +
                            "    \"sposób_zapłaty\": \"PAYU\"\n" +
                            "  }";
        PaymentVerifier paymentVerifier = new PaymentVerifier();
        String result = paymentVerifier.process(paymentFormJson);
        assertEquals(result, "https://www.payu.pl/");
    }
    
    @Test
    public void testProcessInvalid() {
        String paymentFormJson = "{\n" +
                            "    \"id_klienta\": \"1\",\n" +
                            "    \"id_zamowienia\": \"1\",\n" +
                            "    \"sposób_zapłaty\": \"cos\"\n" +
                            "  }";
        PaymentVerifier paymentVerifier = new PaymentVerifier();
        String result = paymentVerifier.process(paymentFormJson);
        assertEquals(result, "Invalid input");
    }
    
}
