

jogadorAtual <- 0;
dadosSorteados <- [];
tiros <- 0;
cerebros <- 0;
passos <- 0;

ENQUANTO (Verdadeiro) FACA:

	escreva("TURNO DO JOGADOR ", listaJogadores[jogadorAtual]);

	PARA i de 0 ate 3 passo 1 FACA
		
		numSorteado <- aleatorio(0, 12);
		dadoSorteado <- listaDados[numSorteado];

		SE(dadoSorteado = 'CPCTPC') ENTAO
			corDado <- 'VERDE';
		SENAOSE(dadoSorteado = 'TPCTPC') ENTAO
			corDado <- 'AMARELO';
		SENAO
			corDado <- 'VERMELHO';
		FIMSE

		escreva("Dado sorteado: ", corDado);

		dadosSorteados[i] <- dadoSorteado;
		
	FIMPARA


	escreva("As faces sorteadas foram: ")

	PARA dadoSorteado em dadosSorteados FACA

		numFaceDado = aleatorio(0, 5);

		SE dadoSorteado[numFaceDado] = "C" ENTAO
			escreva("- CEREBRO (voce comeu um cerebro)");
			cerebros <- cerebros + 1;
		SENAOSE dadoSorteado[numFaceDado] = "T" ENTAO
			escreva("- TIRO (voce levou um tiro)");
			tiros <- tiros + 1;
		SENAO
			escreva("- PASSOS (uma vitima escapou)");
			passos <- passos + 1;
		FIMSE

	FIMPARA
	
	escreva("SCORE ATUAL: ");
	escreva("CEREBROS: ", cerebros);
	escreva("TIROS: ", tiros);

	escreva("AVISO: Voce deseja continuar jogando dados? (s=sim / n=nao)");
	leia(continuarTurno);

	SE (continuarTurno = 'n') ENTAO

		jogadorAtual <- jogadorAtual + 1;
		dadosSorteados <- [];
		tiros <- 0;
		cerebros <- 0;
		passos <- 0;

		SE (jogadorAtual == tamanho(listaJogadores)) ENTAO
			escreva("Finalizando prototipo do jogo...");
			pare;
		FIMSE

	SENÃƒO:
		escreva("Iniciando mais uma rodada do turno atual...");
		dadosSorteados <- [];
	FIMSE

FIMENQUANTO
