package com.example.parcerprojectkostiantyn.Repository;

import com.example.parcerprojectkostiantyn.Models.ParcerModel;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.Optional;

public interface ParcerRepository extends JpaRepository<ParcerModel, Long> {
    void deleteById(Long id);
    Optional<ParcerModel> findModelById(Long id);
}

