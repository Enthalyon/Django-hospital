import { ComponentFixture, TestBed } from '@angular/core/testing';

import { RegistrarFamiliarAsignadoComponent } from './registrar-familiar-asignado.component';

describe('RegistrarFamiliarAsignadoComponent', () => {
  let component: RegistrarFamiliarAsignadoComponent;
  let fixture: ComponentFixture<RegistrarFamiliarAsignadoComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ RegistrarFamiliarAsignadoComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(RegistrarFamiliarAsignadoComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
