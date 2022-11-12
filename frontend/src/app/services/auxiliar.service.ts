import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { environment } from 'src/environments/environment';

@Injectable({
  providedIn: 'root'
})
export class AuxiliarService {
  env: String;
  constructor(private _httpClient: HttpClient) { 
    this.env = environment.app_url;
  }
  obtenerAuxiliar(id: any){
    return this._httpClient.get<any>(`${this.env}/auxiliar/consultar/${id}/`);
  }
}
