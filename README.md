# Engeto-Projekt_3
třetí projekt do Engeto Online Python Akademie

Tento projekt slouží k extrahovani vysledku voleb z roku 2017

Jak ho používat:

1. Stáhněte si soubor projekt_3.py a requirements.txt
2. Nainstalujte knihovny pomocí příkazu pip install -r requirements.txt
3. pusťte program z příkazové řádky
4. Vložte potřebné argumenty:
   - První argument je URL webové stránky (https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2103)
   - Druhý argument je název výstupního CSV souboru (vysledky_kladno.csv)

Příklad
obec Kladno
"https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2103" "vysledky_kladno.csv"
Ukázka výstupního .csv souboru:

code	Location	registered voters	envelopes	valid	Občanská demokratická strana	Řád národa - Vlastenecká unie	Česká str.sociálně demokrat.	STAROSTOVÉ A NEZÁVISLÍ	Komunistická str.Čech a Moravy	Strana zelených	ROZUMNÍ-stop migraci,diktát.EU	Strana svobodných občanů	Blok proti islam.-Obran.domova	Občanská demokratická aliance	Česká pirátská strana
554979	Abertamy	795	366	366	39	2	32	29	24	6	12	7	0	1	36
538001	Andělská Hora	269	188	188	17	0	8	6	13	2	1	0	1	0	18
554995	Bečov nad Teplou	779	440	437	32	9	21	25	35	0	4	6	1	0	35
555029	Bochov	1598	826	819	70	11	83	31	94	7	9	6	0	2	57
506486	Boží Dar	232	172	169	29	1	6	20	2	3	3	2	0	1	22
555045	Božičany	476	239	237	9	0	19	18	19	1	7	1	0	2	22
500101	Bražec	213	94	91	4	0	15	2	7	0	1	1	0	0	5
537870	Březová	440	266	263	22	0	25	15	9	3	0	2	2	2	33
538019	Černava	258	155	155	19	2	5	8	14	0	0	2	0	0	5
506621	Čichalov	143	72	71	4	0	2	11	17	0	2	0	0	0	9
537918	Dalovice	1584	987	983	125	3	45	67	64	15	11	7	1	1	109
538116	Děpoltovice	319	211	209	25	1	8	12	15	2	3	3	0	0	33
500127	Doupovské Hradiště	136	75	74	0	0	4	3	9	0	2	1	0	0	5
538159	Hájek	457	308	306	43	11	20	15	19	1	4	9	2	0	29
555169	Horní Blatná	310	181	180	51	4	6	14	11	1	3	0	0	0	13
551651	Hory	214	127	126	14	1	13	17	5	1	3	3	0	0	10
555185	Hroznětín	1585	856	847	71	0	60	43	76	4	11	7	0	4	73
578011	Chodov	93	52	52	1	0	10	3	3	0	1	1	0	0	2
555207	Chyše	468	286	284	15	0	19	14	20	3	1	0	1	0	23
555215	Jáchymov	2208	1105	1094	122	21	111	45	82	12	9	7	0	1	72
537926	Jenišov	657	451	447	103	1	29	36	18	2	1	5	0	2	54
554961	Karlovy Vary	37610	21332	21182	2232	88	1380	1408	1324	260	169	257	19	78	2532
555258	Kolová	588	368	366	58	1	24	20	16	3	6	2	0	1	55
555304	Krásné Údolí	340	157	155	17	2	2	3	15	0	3	2	0	1	10
578045	Krásný Les	262	177	176	24	5	12	13	7	1	4	5	1	0	12
555347	Kyselka	654	356	353	29	2	14	31	30	4	3	3	1	0	24
555363	Merklín	783	432	426	42	3	25	21	35	11	9	6	1	0	42
537934	Mírová	253	172	172	26	0	11	12	6	1	3	3	0	0	21
555380	Nejdek	6248	3052	3028	260	9	232	136	183	64	35	27	2	3	299
555398	Nová Role	3382	1991	1973	163	10	161	223	112	23	15	30	3	5	178
506494	Nové Hamry	287	203	201	24	0	7	15	17	1	0	11	1	1	14
555428	Ostrov	14090	7635	7577	738	35	500	326	627	96	117	101	23	16	794
537969	Otovice	692	511	506	64	12	23	32	28	2	6	8	2	1	55
555444	Otročín	394	200	195	8	0	15	4	29	0	5	4	2	0	13
555452	Pernink	535	306	305	42	1	14	31	19	5	5	0	0	0	34
556947	Pila	410	268	266	17	3	32	16	22	5	3	1	1	0	25
555479	Potůčky	253	144	142	27	0	15	9	18	2	3	2	0	0	10
555525	Pšov	462	198	198	6	1	19	12	19	1	1	1	0	0	15
555533	Sadov	991	598	590	87	4	29	38	30	3	6	5	0	2	61
538027	Smolné Pece	136	92	92	24	2	5	5	0	5	0	1	0	0	3
555550	Stanovice	501	277	274	25	1	8	23	21	1	2	5	0	1	25
555584	Stráž nad Ohří	482	256	255	13	0	12	10	31	5	2	0	0	0	22
555592	Stružná	450	247	247	12	0	4	23	16	0	4	3	1	0	26
555614	Šemnice	517	292	290	47	2	13	15	25	9	4	7	0	1	27
555622	Štědrá	467	216	213	8	0	10	4	26	4	8	2	1	0	16
537845	Teplička	92	62	61	7	0	2	0	2	1	1	0	0	0	7
555657	Toužim	2974	1493	1483	130	5	125	41	165	15	11	24	0	1	139
555681	Útvina	460	271	268	6	1	15	7	43	7	3	2	0	0	27
555690	Valeč	286	165	164	6	0	6	14	20	7	5	0	0	0	25
555703	Velichov	433	263	261	14	1	17	18	16	3	4	2	3	0	17
555711	Verušičky	403	178	178	4	2	6	50	33	0	8	1	0	1	5
555738	Vojkovice	505	267	266	6	0	20	12	20	3	2	0	0	0	41
566675	Vrbice	152	63	63	1	0	4	7	13	0	0	0	0	0	1
578029	Vysoká Pec	274	168	168	9	2	2	11	14	9	0	0	0	0	25
555762	Žlutice	1998	974	963	58	6	61	38	97	10	9	7	1	2	58
![image](https://github.com/AleksGus/Engeto-Projekt_3/assets/128379968/24c212fa-c983-4e4d-8261-393dc9aeddd0)


