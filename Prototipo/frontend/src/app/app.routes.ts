import { Routes } from '@angular/router';
import { AdminComponent } from './admin/admin.component';
import { GestionarHabitacionesComponent } from './admin/gestionar-habitaciones/gestionar-habitaciones.component';
import { CrearHabitacionComponent } from './admin/crear-habitacion/crear-habitacion.component';
import { HabitacionDetalleComponent } from './habitacion-detalle/habitacion-detalle.component';
import { LoginComponent } from './login/login.component';
import { RegistroComponent } from './registro/registro.component';
import { ReservasComponent } from './reservas/reservas.component';
import { HabitacionesComponent } from './habitaciones/habitaciones.component';


export const routes: Routes = [
    { path: '', redirectTo: '/habitaciones', pathMatch: 'full' },
    { path: 'admin', component: AdminComponent },
    { path: 'admin/gestionar-habitaciones', component: GestionarHabitacionesComponent },
    { path: 'admin/crear-habitacion', component: CrearHabitacionComponent },
    { path: 'habitacion/:id', component: HabitacionDetalleComponent },
    { path: 'login', component: LoginComponent },
    { path: 'registro', component: RegistroComponent },
    { path: 'reservas', component: ReservasComponent },
    { path: 'habitaciones', component: HabitacionesComponent },

];
