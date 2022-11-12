import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HeaderComponent } from './home/header/header.component';
import { CrearRegistroSignosVitalesComponent } from './paciente/crear-registro-signos-vitales/crear-registro-signos-vitales.component';
import { ActualizarDatosPersonalesComponent } from './paciente/actualizar-datos-personales/actualizar-datos-personales.component';
import { ConsultarHistoriaComponent } from './paciente/consultar-historia/consultar-historia.component';
import { ModificarRegistroSignosVitalesComponent } from './personal/modificar-registro-signos-vitales/modificar-registro-signos-vitales.component';
import { ConsultarPacientesComponent } from './personal/consultar-pacientes/consultar-pacientes.component';
import { RegistrarPacienteComponent } from './auxiliar/registrar-paciente/registrar-paciente.component';
import { RegistrarFamiliarAsignadoComponent } from './auxiliar/registrar-familiar-asignado/registrar-familiar-asignado.component';
import { RegistrarPersonalDeSaludComponent } from './auxiliar/registrar-personal-de-salud/registrar-personal-de-salud.component';
import { AsignarPersonalComponent } from './auxiliar/asignar-personal/asignar-personal.component';

//services
import { UtilsService } from "./services/utils.service";
import { AuxiliarService } from './services/auxiliar.service';
import { FamiliarAsignadoService } from './services/familiar-asignado.service';
import { PacienteService } from './services/paciente.service';
import { ProfesionalService } from './services/profesional.service';
import { SignosVitalesService } from './services/signos-vitales.service';
import { UsuarioService } from './services/usuario.service';
import { LoginComponent } from './home/login/login.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

//material
import { HttpClientModule, HTTP_INTERCEPTORS } from '@angular/common/http';
import { FormsModule } from '@angular/forms';
import { MainComponent } from './home/main/main.component';
import { MatSnackBarModule } from '@angular/material/snack-bar';
import { MatIconModule } from '@angular/material/icon';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatSelectModule } from '@angular/material/select';
import { MatInputModule } from '@angular/material/input';
import { MatButtonModule } from '@angular/material/button';
import { TokenInterceptorService } from './services/token-interceptor.service';
import { WelcomeComponent } from './home/welcome/welcome.component';

@NgModule({
  declarations: [
    AppComponent,
    HeaderComponent,
    CrearRegistroSignosVitalesComponent,
    ActualizarDatosPersonalesComponent,
    ConsultarHistoriaComponent,
    ModificarRegistroSignosVitalesComponent,
    ConsultarPacientesComponent,
    RegistrarPacienteComponent,
    RegistrarFamiliarAsignadoComponent,
    RegistrarPersonalDeSaludComponent,
    AsignarPersonalComponent,
    LoginComponent,
    MainComponent,
    WelcomeComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    FormsModule,
    HttpClientModule,
    MatSnackBarModule,
    MatIconModule,
    MatFormFieldModule,
    MatSelectModule,
    MatInputModule,
    MatButtonModule,
  ],
  providers: [
    AuxiliarService,
    FamiliarAsignadoService,
    PacienteService,
    ProfesionalService,
    SignosVitalesService,
    UsuarioService,
    UtilsService,
    {
      provide: HTTP_INTERCEPTORS,
      useClass: TokenInterceptorService,
      multi: true,
    },
  ],
  bootstrap: [AppComponent],
})
export class AppModule {}
