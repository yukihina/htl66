# ANÁLISIS COMPLETO: PUNTOS DE AMBER (EP01-EP05)

## RESUMEN EJECUTIVO

**¿Es posible obtener trust >= 35 Y cor >= 20?**

✅ **SÍ, ES COMPLETAMENTE POSIBLE**

- Máximo Trust alcanzable: **50 puntos**
- Máximo Cor alcanzable: **40.5 puntos**
- Ruta Balance óptima: **41 trust + 40.5 cor**

**NOTA**: El threshold de corruption fue ajustado de 10 a 20 para mejor balance del juego.

---

## INFORMACIÓN DEL SISTEMA

Según `scripts/systems/core.rpy`:
- **Multiplicador Trust de Amber**: 1.0x
- **Multiplicador Cor de Amber**: 1.5x
- Los puntos base en el código se multiplican automáticamente por estos factores

---

## ANÁLISIS DETALLADO POR EPISODIO

### EPISODIO 1 (ep01.rpy)

**Máximo Trust**: 4 puntos
**Máximo Cor**: 4.5 puntos
**Combinado**: 4 trust + 4.5 cor

#### Decisiones Trust:
1. **"Go after Amber"** (línea 2483): +1 trust
   - vs "Comfort Antonella": 0 puntos

2. **"Lie to Amber"** (línea 2535): +1 trust
   - vs "Tell truth": -1 trust
   - Solo si elegiste "Go after Amber"

3. **"Reassure Amber"** (línea 2825): +1 trust
   - vs "Be evasive": -1 trust

4. **"Stay"** (línea 3453): +1 trust
   - vs "Leave": -1 trust

#### Decisiones Cor:
5. **"Yes"** (línea 3720): +3 cor base × 1.5 = **+4.5 cor**
   - Solo disponible si elegiste "Stay" (ep01_ambtalk = True)

---

### EPISODIO 2

❌ **No hay puntos de Amber en EP02**

---

### EPISODIO 3 (ep03.rpy)

**Máximo Trust (ruta pura)**: 22 puntos + 4.5 cor
**Ruta Balance**: 16 trust + 10.5 cor

#### Decisiones:
1. **"Focus on breasts"**: +1 cor base × 1.5 = **+1.5 cor**
   - vs "Listen to Amber": +2 trust

2. **"Listen to Amber's feelings"** (línea 601): **+5 trust**
   - vs "Refuse": -5 trust

3. **"Tell her to stay"** (línea 733): **+3 trust**
   - vs "Tell her to leave": -3 trust

4. **"Accompany to pool"** (línea 872): **+5 trust**
   - vs "Decline": -5 trust

5. **"Get sweater"** (línea 1487): **+2 trust**
   - vs "Forget sweater": +3 cor × 1.5 = +4.5 cor, -2 trust

6. **"Invite Amber night"** (línea 1600): **+3 trust**

7. **"Respect Amber's wishes"** (líneas 2048): +3 cor × 1.5 = **+4.5 cor** + **+2 trust**
   - vs "Insist": -1 cor × 1.5 = -1.5 cor, -5 trust

8. **"Surprise Amber"** (línea 2216): +1 cor × 1.5 = **+1.5 cor**

9. **"Kiss Amber"** (línea 2479): +1 cor × 1.5 = **+1.5 cor**

#### Ruta Balance Recomendada EP03:
- Listen to Amber: +2 trust
- Listen feelings: +5 trust
- Tell stay: +3 trust
- Accompany pool: +5 trust
- Forget sweater: +4.5 cor, -2 trust
- Invite night: +3 trust
- Respect wishes: +4.5 cor, +2 trust
- **TOTAL**: 16 trust + 10.5 cor

---

### EPISODIO 4

**ep04_sms.rpy + ep04.rpy**

**Máximo Trust**: 10 puntos + 3 cor
**Máximo Cor**: 10 trust + 16.5 cor

#### ep04_sms.rpy:
1. **"Accept help"** (línea 1189): **+5 trust**
   - vs "Deny": -5 trust

2. **"View sexy back"** (línea 1213): +1 cor × 1.5 = **+1.5 cor**

3. **"View cosplay back"** (línea 1278): +1 cor × 1.5 = **+1.5 cor**

4. **"Stay for reward"** (línea 1363): +3 cor × 1.5 = **+4.5 cor**

5. **"Accept game"** (línea 1442): +3 cor × 1.5 = **+4.5 cor**

#### ep04.rpy:
6. **Bugfix automático** (líneas 2399+2402): +1 cor × 1.5 = **+1.5 cor** + **+2 trust**

7. **"Answer You"** (líneas 5239-5241): +1 cor × 1.5 = **+1.5 cor** + **+2 trust**
   - vs "LEDs": -1 cor, -2 trust

8. **"Cum on tits"** (líneas 5591-5593): +1 cor × 1.5 = **+1.5 cor** + **+1 trust**
   - vs "Cum on face": +1 cor × 1.5, -2 trust

#### Ruta Balance Recomendada EP04:
- Accept help: +5 trust
- View sexy: +1.5 cor
- View cosplay: +1.5 cor
- Stay reward: +4.5 cor
- Accept game: +4.5 cor
- Bugfix: +1.5 cor + 2 trust
- Answer You: +1.5 cor + 2 trust
- Cum tits: +1.5 cor + 1 trust
- **TOTAL**: 10 trust + 16.5 cor

---

### EPISODIO 5

**ep05.rpy + ep05_end.rpy**

**Máximo Trust (ruta pura)**: 14 puntos
**Ruta Balance**: 11 trust + 9 cor

#### ep05.rpy:
1. **"Apologize"** (línea 408): **+5 trust** + reduce 1 strike
   - vs "Don't apologize": -5 trust

2. **"Accept advances"** (línea 508): +3 cor × 1.5 = **+4.5 cor**
   - vs "Reject": -3 cor

3. **"Defend Amber"** (línea 1400): **+2 trust**
   - vs "Ignore": -2 trust

#### ep05_end.rpy:
4. **"Show compassion"** (línea 1127): **+2 trust**
   - vs "Stay detached": -2 trust

5. **"Be romantic"** (línea 1242): **+5 trust**
   - vs "Be passionate": +2 trust + 3 cor × 1.5 = +4.5 cor
   - vs "Pull away": -5 trust + 1 strike

#### Ruta Balance Recomendada EP05:
- Apologize: +5 trust
- Accept advances: +4.5 cor
- Defend: +2 trust
- Compassion: +2 trust
- Be passionate: +2 trust + 4.5 cor
- **TOTAL**: 11 trust + 9 cor

---

## TABLA RESUMEN

| Episodio | MAX Trust | MAX Cor | Balance Trust | Balance Cor |
|----------|-----------|---------|---------------|-------------|
| EP01     | 4         | 4.5     | 4             | 4.5         |
| EP02     | 0         | 0       | 0             | 0           |
| EP03     | 22        | 4.5     | 16            | 10.5        |
| EP04     | 10        | 3       | 10            | 16.5        |
| EP05     | 14        | 0       | 11            | 9           |
| **TOTAL**| **50**    | **12**  | **41**        | **40.5**    |

---

## CONCLUSIONES

### ¿Es posible obtener trust >= 35 Y cor >= 20?

**✅ SÍ, CON LA RUTA BALANCE:**

```
EP01: 4 trust + 4.5 cor
EP03: 16 trust + 10.5 cor
EP04: 10 trust + 16.5 cor
EP05: 11 trust + 9 cor
──────────────────────────
TOTAL: 41 trust + 40.5 cor
```

**Resultado:**
- ✅ Trust = 41 >= 35 **(SOBRAN 6 PUNTOS)**
- ✅ Cor = 40.5 >= 20 **(SOBRAN 20.5 PUNTOS)**

### Margen de Error

El jugador puede perder:
- Hasta **6 puntos de trust** y aún alcanzar threshold (permite ~12% error)
- Hasta **20.5 puntos de cor** y aún alcanzar threshold (permite ~50% error)

### Recomendaciones

Los thresholds fueron **BALANCEADOS** para mejor game design:
- `rm.get("amber", "trust") >= 35` ✅ **70% del máximo** - Requiere compromiso con ruta love
- `rm.get("amber", "cor") >= 20` ✅ **50% del máximo** - Requiere compromiso con ruta corruption

**THRESHOLDS AJUSTADOS PARA MEJOR BALANCE** (cor ajustado de 10 a 20).

Si los jugadores no están alcanzando estos valores, puede deberse a:
1. Decisiones subóptimas en la historia
2. Sistema de strikes bloqueando opciones
3. Bugs en la implementación del sistema de puntos
4. Pérdida de puntos por decisiones negativas

---

## VERIFICACIÓN EN EP06

El archivo `scripts/ep06/ep06.rpy` línea 714 muestra:
```renpy
"[Corruption] Show me." if ss.get("amber", "strike") == 0 and rm.get("amber", "cor") >= 20:
```

Y línea 761 muestra:
```renpy
"[Love] You see me." if ss.get("amber", "strike") == 0 and rm.get("amber", "trust") >= 35:
```

Ambos thresholds son **totalmente alcanzables** con los **40.5 cor** y **50 trust** disponibles:
- **Corruption path**: Requiere 50% del máximo (20/40.5) - Balanceado
- **Love path**: Requiere 70% del máximo (35/50) - Más estricto, apropiado para ruta emocional

---

**Fecha de análisis:** 2025-12-01
**Archivos analizados:** ep01.rpy, ep01_sms.rpy, ep02.rpy, ep03.rpy, ep03_sms.rpy, ep04.rpy, ep04_sms.rpy, ep05.rpy, ep05_end.rpy, ep05_sms.rpy
