package backend.backendRealisation;

import backend.backendRealisation.dao.DatabaseAccess;
import backend.backendRealisation.dao.DatabaseAccessImpl;
import backend.backendRealisation.interfaces.PracKReal;
import backend.backendRealisation.services.OrderListService;
import backend.backendRealisation.services.OrderListServiceImpl;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;

@SpringBootApplication
public class BackendRealisationApplication {

    public static void main(String[] args) {
        SpringApplication.run(BackendRealisationApplication.class, args);
    }

    @Bean
    public OrderListService orderListService(){
        return new OrderListServiceImpl(databaseAccess());
    }

    @Bean
    public DatabaseAccess databaseAccess(){
        return new DatabaseAccessImpl();
    }

}
