import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { AuxiliarService } from 'src/app/services/auxiliar.service';
import { FamiliarAsignadoService } from 'src/app/services/familiar-asignado.service';
import { PacienteService } from 'src/app/services/paciente.service';
import { ProfesionalService } from 'src/app/services/profesional.service';
import { UsuarioService } from 'src/app/services/usuario.service';
import { UtilsService } from 'src/app/services/utils.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  data: any = {}
  rolesList: any[];
  selectedId: any;

  constructor(
    private _usuarioServicio: UsuarioService,
    private _familiarServicio: FamiliarAsignadoService,
    private _pacienteServicio: PacienteService,
    private _profesionalServicio: ProfesionalService,
    private _auxiliarServicio: AuxiliarService,
    private _utils: UtilsService,
    private _router: Router
  ) { 
    this.rolesList = [
      {name: 'Paciente', value: 0},
      {name: 'Personal de Salud', value: 1}, 
      {name: 'Familiar', value: 2}, 
      {name: 'Auxiliar', value: 3}
    ]
  }

  ngOnInit(): void {
  }
  async loggear(){
    if(this.data.email && this.data.password && this.selectedId != undefined){
      this._usuarioServicio.login(this.data).subscribe( 
        (res) => {    
          localStorage.setItem("token", res.access);
          this._usuarioServicio.getUserByToken().subscribe(
            (res) => {
              switch (this.selectedId) {
                case 0:
                  this._pacienteServicio.obtenerPaciente(res.id).subscribe(
                    (res) => {
                      console.log(res);
                      localStorage.setItem("data", JSON.stringify(res));
                      localStorage.setItem("permission", "0");
                      this._router.navigate([`/welcome`]);
                      this._utils.openSnackBarSuccessfully("login exitoso!")
                    },
                    (err) => {
                      this._utils.openSnackBarError("El usuario indicado no pertenece a este rol")
                      localStorage.clear();
                    }
                  )
                  break;
                case 1:
                  this._profesionalServicio.obtenerProfesional(res.id).subscribe(
                    (res) => {
                      localStorage.setItem("data", JSON.stringify(res));
                      localStorage.setItem("permission", "1");
                      this._router.navigate([`/welcome`]);
                      this._utils.openSnackBarSuccessfully("login exitoso!")
                    },
                    (err) => {
                      this._utils.openSnackBarError("El usuario indicado no pertenece a este rol")
                      localStorage.clear();
                    }
                  )                  
                  break;
                case 2:
                  this._familiarServicio.obtenerFamiliar(res.id).subscribe(
                    (res) => {
                      localStorage.setItem("data", JSON.stringify(res));
                      localStorage.setItem("permission", "2");
                      this._router.navigate([`/welcome`]);
                      this._utils.openSnackBarSuccessfully("login exitoso!")
                    },
                    (err) => {
                      this._utils.openSnackBarError("El usuario indicado no pertenece a este rol")
                      localStorage.clear();
                    }
                  )                  
                  break;
                case 3:
                  this._auxiliarServicio.obtenerAuxiliar(res.id).subscribe(
                    (res) => {
                      localStorage.setItem("data", JSON.stringify(res));
                      localStorage.setItem("permission", "3");
                      this._router.navigate([`/welcome`]);
                      this._utils.openSnackBarSuccessfully("login exitoso!")
                    },
                    (err) => {
                      this._utils.openSnackBarError("El usuario indicado no pertenece a este rol")
                      localStorage.clear();
                    }
                  )                  
                  break;                            
                default:
                  this._utils.openSnackBarError("Error al loggear")
                  break;
              }
            }, 
            (err) => {
              this._utils.openSnackBarError("Error al loggear")
            }
          )   
        },
        (err) => {
          console.log(err);
          
          this._utils.openSnackBarError("Usuario o contraseña incorrecta");
        }
      )
    } else {
      this._utils.openSnackBarError("todos los campos son obligatorios");
    }
  }
}
