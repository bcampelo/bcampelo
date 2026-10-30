# Notchestra

App nativo de Mac que faz seus agentes de IA trabalharem juntos.

Você dá um pedido grande. O maestro divide em tarefas, escolhe o agente e o modelo de cada uma e mostra o plano pra você aprovar. As tarefas rodam em paralelo, cada uma no seu git worktree. Um agente executa, outro de outra família revisa, e se a revisão reprovar o feedback volta pra quem executou. No fim o maestro confere o diff inteiro contra o pedido e abre o pull request.

Tudo acompanhado numa ilha no notch do Mac.

![Palco da orquestra](docs/screens/fase-4-2/01-palco-orquestra-escuro.png)

## O que tem

- **Palco da orquestra.** Cada agente é um músico no seu lugar, com a tarefa que está tocando, o terminal ao vivo e o estado da revisão.
- **Ilha no notch.** Status da execução sem abrir janela. Em Mac sem notch ela vira um painel flutuante.
- **Maestro e roteador.** O maestro planeja a partitura. O roteador decide executor e revisor por tipo e complexidade da tarefa, pula agente sem cota e explica cada escolha.
- **Custo.** Estimativa antes de aprovar e custo real no fim de cada execução.
- **Limites.** Uso de Claude Code, Kiro, Codex e Gemini na barra lateral, com aviso antes de começar.
- **Portão de testes e PR.** Roda os testes do projeto antes da revisão final e abre o pull request com `gh`.
- **Sessões interativas.** Dá pra assumir uma tarefa num terminal e conversar com o agente direto.

![Ilha no notch](docs/screens/fase-4-2/02-palco-orquestra-recolhido-escuro.png)

## Agentes

Qualquer CLI que aceite prompt em modo não interativo. O primeiro uso detecta as CLIs instaladas e monta a configuração sozinho. Exemplos para Claude Code, Kiro, Codex e Gemini em `examples/`.

## Requisitos

- macOS 14 ou superior
- Xcode 16 ou superior, com o Metal Toolchain (`xcodebuild -downloadComponent MetalToolchain`)
- As CLIs dos agentes instaladas e logadas

## Rodando

```bash
brew install xcodegen
scripts/build-app.sh
open App/build/Build/Products/Debug/Notchestra.app
```

O núcleo também roda pelo terminal.

```bash
swift build
swift run notchestra --help
```

## Como foi feito

O app foi construído com os próprios agentes que ele orquestra. Kiro executando, Claude Code revisando, em fases curtas. As decisões de arquitetura estão em `docs/decisoes/`, o diário de cada sessão em `docs/PROGRESSO.md` e os prompts de cada fase em `docs/prompts/`.

## Stack

Swift · SwiftUI · AppKit · Swift Package Manager · XcodeGen · git worktrees

## Licença

MIT
