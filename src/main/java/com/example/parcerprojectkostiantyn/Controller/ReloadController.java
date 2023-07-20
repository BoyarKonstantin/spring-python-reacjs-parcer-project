package com.example.parcerprojectkostiantyn.Controller;

import com.example.parcerprojectkostiantyn.ParcerProjectKostiantynApplication;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.SpringApplication;
import org.springframework.context.ConfigurableApplicationContext;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/actuator")
@CrossOrigin
public class ReloadController {

    private final ConfigurableApplicationContext context;

    @Autowired
    public ReloadController(ConfigurableApplicationContext context) {
        this.context = context;
    }

    @PostMapping("/restart")
    public void restart() {
        Thread thread = new Thread(() -> {
            context.close();
            SpringApplication.run(ParcerProjectKostiantynApplication.class);
        });
        thread.setDaemon(false);
        thread.start();
    }
}
