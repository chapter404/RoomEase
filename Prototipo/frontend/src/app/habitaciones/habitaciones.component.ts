import { Component, OnInit } from '@angular/core';
import { RouterLink } from '@angular/router';
import { CommonModule } from '@angular/common';
import { HabitacionesService } from '../services/habitaciones.service';
@Component({
  selector: 'app-habitaciones',
  standalone: true,
  imports: [RouterLink, CommonModule],
  templateUrl: './habitaciones.component.html',
  styleUrl: './habitaciones.component.css'
})
export class HabitacionesComponent implements OnInit {

  habitaciones: any[] = []; 

  constructor(private habitacionesService: HabitacionesService) {}

  ngOnInit() {
    this.habitacionesService.getHabitaciones().subscribe((data) => {
      this.habitaciones = data;
    }, (error) => {
      console.error('Error al obtener habitaciones:', error);
    });
  }
}
