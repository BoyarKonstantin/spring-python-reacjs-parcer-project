package com.example.parcerprojectkostiantyn.Controller;

import com.example.parcerprojectkostiantyn.Models.ParcerModel;
import com.example.parcerprojectkostiantyn.Service.ParcerService;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/parcer")
@CrossOrigin
public class ParcerController {

    public final ParcerService parcerService;

    public ParcerController(ParcerService parcerService){
        this.parcerService = parcerService;
    }

    @GetMapping("/all")
    public ResponseEntity<List<ParcerModel>> getAllModels(){
        List<ParcerModel> parcerModelList = parcerService.findAll();
        return new ResponseEntity<>(parcerModelList, HttpStatus.OK);
    }
    @PostMapping("/add")
    public ResponseEntity<ParcerModel> addModel(@RequestBody ParcerModel parcerModel){
        ParcerModel addModel = parcerService.addModel(parcerModel);
        return new ResponseEntity<>(addModel, HttpStatus.CREATED);
    }
    @DeleteMapping("/delete/{id}")
    public ResponseEntity<?> deleteModel(@PathVariable("id") Long id){
        parcerService.deleteModel(id);
        return new ResponseEntity<>(HttpStatus.OK);
    }
    @PutMapping("/update")
    public ResponseEntity<ParcerModel> updateModel(@RequestBody ParcerModel parcerModel){
        ParcerModel updateModel = parcerService.updateModel(parcerModel);
        return new ResponseEntity<>(updateModel, HttpStatus.OK);
    }
}
