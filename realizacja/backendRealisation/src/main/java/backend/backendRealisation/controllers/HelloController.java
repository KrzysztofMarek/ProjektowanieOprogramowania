package backend.backendRealisation.controllers;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

/**
 * Created by Piotr on 2018-10-22.
 */
@RestController
public class HelloController {

    @RequestMapping("/")
    public String index() {
        return "Witaj";
    }

}