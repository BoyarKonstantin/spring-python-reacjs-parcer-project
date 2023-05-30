package com.example.parcerprojectkostiantyn;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cache.annotation.EnableCaching;

@EnableCaching
@SpringBootApplication
public class ParcerProjectKostiantynApplication {

    public static void main(String[] args) {
        SpringApplication.run(ParcerProjectKostiantynApplication.class, args);
    }

}
