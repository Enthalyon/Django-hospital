import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { environment } from 'src/environments/environment';

@Injectable({
  providedIn: 'root'
})
export class UsuarioService {

  env: String;
  constructor(private _httpClient: HttpClient) { 
    this.env = environment.app_url;
  }
  crearUsuario(data: any){
    return this._httpClient.post<any>(`${this.env}/usuario/registrar/`, data);
  }
  updateUser(data: any){
    return this._httpClient.put<any>(`${this.env}usuarios`, data);
  }
  login(data: any){
    return this._httpClient.post<any>(`${this.env}/login/`, data);
  }
  getUserByToken(){
    return this._httpClient.get<any>(`${this.env}/usuario/consultar/token/`);
  }
  getToken(){
    return localStorage.getItem('token')
  }
  loggedIn() {
    return !!localStorage.getItem('token');
  }
}
