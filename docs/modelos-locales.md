# Modelos locales (experimento descartado)

Se intentó usar Claude Code con modelos locales servidos por **Ollama** (`ollama launch claude --model ...`) para no depender de un plan de pago. El experimento se descartó.

## Equipo

Tarjeta gráfica RTX 4070 con 12 GB de VRAM.

## Qué se probó y qué pasó

| Prueba | Resultado |
|---|---|
| **GLM-4.7-Flash** (19 GB) | No cabe en 12 GB de VRAM: corría al 67 % en CPU y era muy lento |
| Contexto por defecto de Ollama (4096 tokens) | El modelo **no veía las herramientas** del MCP. Se subió con la variable `OLLAMA_CONTEXT_LENGTH`; hay que reiniciar Ollama y las terminales para que surta efecto |
| Modo *auto* de Claude Code | Usa el mismo modelo como clasificador de permisos. Con un modelo lento bloqueaba herramientas con "Classifier unavailable". Hubo que desactivarlo |
| **Qwen3.5-9B** con 32 000 tokens de contexto | Las tareas largas se cortaban con "Server error mid-response". El registro mostraba 32 671 de 32 768 tokens y `truncated = 1` |

## Conclusión

En ese hardware **no es viable**. Una práctica completa necesita mucho contexto (enunciado, árbol del checklist, salidas de la CLI) y un modelo capaz de manejar más de cien herramientas MCP. El proyecto usa Claude Code con los modelos de Anthropic: Sonnet para tareas normales y Opus para lo complejo.
