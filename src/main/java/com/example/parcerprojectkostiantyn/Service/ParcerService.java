package com.example.parcerprojectkostiantyn.Service;

import com.example.parcerprojectkostiantyn.Models.ParcerModel;
import com.example.parcerprojectkostiantyn.Repository.ParcerRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.cache.annotation.Cacheable;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;
import java.util.UUID;

@Service
@Transactional
public class ParcerService {

    private final ParcerRepository parcerRepository;
    @Autowired
    public ParcerService(ParcerRepository parcerRepository){
        this.parcerRepository = parcerRepository;
    }
    public ParcerModel addModel(ParcerModel parcerModel){
        parcerModel.setModelCode(UUID.randomUUID().toString());
        return parcerRepository.save(parcerModel);
    }
    @Cacheable(cacheNames = {"allModel"})
    public List<ParcerModel> findAll(){
        return parcerRepository.findAll();
    }
    public ParcerModel updateModel(ParcerModel parcerModel){
        return parcerRepository.save(parcerModel);
    }

    public void deleteModel(Long id){
        parcerRepository.deleteById(id);
    }


}
