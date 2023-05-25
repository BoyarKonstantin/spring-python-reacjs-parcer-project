package com.example.parcerprojectkostiantyn.Models;


import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.Id;
import lombok.*;

@Entity
@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@ToString
public class ParcerModel {

    @Id()
    @GeneratedValue
    private int id;
    private String shopName;
    private String date;
    private String price;
    private String available;
    private String modelCode;
    private String modelName;
    private String modelLink;
    private String requiedPrice;
    private String dumpingStatus;


}
