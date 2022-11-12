import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AsignarPersonalComponent } from './auxiliar/asignar-personal/asignar-personal.component';
import { RegistrarFamiliarAsignadoComponent } from './auxiliar/registrar-familiar-asignado/registrar-familiar-asignado.component';
import { RegistrarPacienteComponent } from './auxiliar/registrar-paciente/registrar-paciente.component';
import { RegistrarPersonalDeSaludComponent } from './auxiliar/registrar-personal-de-salud/registrar-personal-de-salud.component';
import { LoginComponent } from './home/login/login.component';
import { MainComponent } from './home/main/main.component';
import { WelcomeComponent } from './home/welcome/welcome.component';
import { ActualizarDatosPersonalesComponent } from './paciente/actualizar-datos-personales/actualizar-datos-personales.component';
import { ConsultarHistoriaComponent } from './paciente/consultar-historia/consultar-historia.component';
import { CrearRegistroSignosVitalesComponent } from './paciente/crear-registro-signos-vitales/crear-registro-signos-vitales.component';
import { ConsultarPacientesComponent } from './personal/consultar-pacientes/consultar-pacientes.component';
import { ModificarRegistroSignosVitalesComponent } from './personal/modificar-registro-signos-vitales/modificar-registro-signos-vitales.component';

const routes: Routes = [
  {
    path: '',
    component: MainComponent,
    pathMatch: 'full'
  },
  {
    path: 'welcome',
    component: WelcomeComponent,
    pathMatch: 'full'
  },
  {
    path: 'login',
    component: LoginComponent,
    pathMatch: 'full'
  },
  {
    path: 'paciente/actualizar-datos',
    component: ActualizarDatosPersonalesComponent,
    pathMatch: 'full'
  },
  {
    path: 'paciente/consultar-historia/:id',
    component: ConsultarHistoriaComponent,
    pathMatch: 'full'
  },
  {
    path: 'paciente/consultar-historia',
    component: ConsultarHistoriaComponent,
    pathMatch: 'full'
  },
  {
    path: 'paciente/crear-registro-signos-vitales',
    component: CrearRegistroSignosVitalesComponent,
    pathMatch: 'full'
  },
  {
    path: 'paciente/crear-registro-signos-vitales/:id',
    component: CrearRegistroSignosVitalesComponent,
    pathMatch: 'full'
  },
  {
    path: 'auxiliar/registrar-paciente',
    component: RegistrarPacienteComponent,
    pathMatch: 'full'
  },
  {
    path: 'auxiliar/registrar-familiar-asignado',
    component: RegistrarFamiliarAsignadoComponent,
    pathMatch: 'full'
  },
  {
    path: 'auxiliar/asignar-personal',
    component: AsignarPersonalComponent,
    pathMatch: 'full'
  },
  {
    path: 'auxiliar/registrar-personal-de-salud',
    component: RegistrarPersonalDeSaludComponent,
    pathMatch: 'full'
  },
  {
    path: 'personal/consultar-pacientes',
    component: ConsultarPacientesComponent,
    pathMatch: 'full'
  },
  {
    path: 'personal/modificar-registro-signos-vitales',
    component: ModificarRegistroSignosVitalesComponent,
    pathMatch: 'full'
  },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
