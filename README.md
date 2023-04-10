# LaTeX Template English

[Download current PDF](../-/jobs/artifacts/master/download?job=build)

> For the Pipeline build to work, the Variable `MAIN_FILE_NAME` in [GitLab CI File](./.gitlab-ci.yml) has to be set if the file name of `btmt_name.tex` is changed

## Linguistic Conventions in the Context of the C&M Software Development Process

All artifacts created during the C&M software development process are written in English.
This also applies to the features created in the analysis phase, since it is assumed that the user of a software system developed by C&M is an English speaker.
American English is used throughout the thesis.

An important quality aspect to be considered in software development is the consistent spelling of the introduced terms during development.
Two levels must be distinguished here: The level of ("natural", English) language and the level of (formal, developmental) artefacts.
An example of a term at the language level is "Todo List Management".
As a C&M convention that terms are written on the artifact level in the so-called CamelCase notation, in this example "TodoListManagement".

## Top Literature

Each top literature publication (roughly 3 to 5, each should be stored as a PDF document in the folder "2-1.Top_Literature") is described in one section. The description should be structured as follows: First, the most relevant part of the publication contributing to your own work is outlined in (around one) sentence. In the following (around one to three) sentences the relationships to your own work are stressed. Such relationships may concern

	i. the problem area
	ii. the method that is described in the publication in order to solve the problem and which is used in your own work,
	iii. deficiencies of the solution method that are tackled in your own work,
	iv. some other conceptual or technical aspects that are relevant for your own work.

Any further relevant part of the publication is described in a further paragraph which is structured as the above paragraph. Each description of a publication belonging to the top literature is completed by an assessment of the publication quality.

## LaTex Hints

### Citations
The demonstrator usually uses components that have been developed earlier by C&M.

```latex
\begin{quote}
\textit{``A microservice is a cohesive, independent process interacting via messages``}
\end{quote}
\begin{quote}
\textit{``fictive book quote.'', \cite[S.~99]{Be02}}
\end{quote}
```

### Inserting Graphics
Images are created with PowerPoint in the image document and saved as .png in the "figures" folder.
Inserting and referencing the figure is done by a reference: Figure `\ref{fig:example}`.
> Note: The title is the same as the title of the PowerPoint figure!

```latex
\begin{figure}[h]
	\centering
	\includegraphics[width=0.8\textwidth]{figures/example_figure.png}
	\caption{Example of a Figure}
	\label{fig:example}
\end{figure}
```

### Inserting Tables
```latex
\begin{table}[H] %Hinweis: Das [H] ist aus dem float-Paket und sorgt dafür, dass die Tabelel an Ort und Stelle gezeichnet wird, wo diese auch defniert ist.
	\centering
	\begin{tabular}{ | l | p{7cm} | }
		\hline
		\textbf{Heading} & \textbf{Further Heading} \\
		\hline
		 Entry & Example of an entry \\
		\hline
		 Entry & Example of a further entry \\
	 	\hline
	\end{tabular}
	\caption{Example of a Table}
	\label{tab:example_table}
\end{table}
```

### Writing Cucumber Features in LaTex
Features are included in the LaTeX code as a special listing and referenced in the text using the feature command.

```latex
\begin{lstlisting}[caption = {Template for a Story and Scenarios According to BDD}, label = {fea:example_feature}, style = kit-cm, language = Gherkin]
Title (one line describing the story)
 
Narrative:
As a [role]
I want [feature]
So that [benefit]
 
Acceptance Criteria: (presented as Scenarios)
 
Scenario 1: Title
Given [context]
  And [some more context]...
When  [event]
Then  [outcome]
  And [another outcome]...
 
Scenario 2: ...
\end{lstlisting}
```