# React + Vite

This template provides a minimal setup to get React working in Vite with HMR and some ESLint rules.

Currently, two official plugins are available:

- [@vitejs/plugin-react](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react) uses [Oxc](https://oxc.rs)
- [@vitejs/plugin-react-swc](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react-swc) uses [SWC](https://swc.rs/)

## React Compiler

The React Compiler is not enabled on this template because of its impact on dev & build performances. To add it, see [this documentation](https://react.dev/learn/react-compiler/installation).

## Expanding the ESLint configuration

If you are developing a production application, we recommend using TypeScript with type-aware lint rules enabled. Check out the [TS template](https://github.com/vitejs/vite/tree/main/packages/create-vite/template-react-ts) for information on how to integrate TypeScript and [`typescript-eslint`](https://typescript-eslint.io) in your project.


Read me starts here:

1. Clone the repository
2. Install Node.js
3. Install Python
4. Install Android Studio (if working on mobile)

5. Copy backend/.env.example to backend/.env        
#This is for the API, you need the key, endpoint, your email to send the warning message and your APP password (different password from your account)

6. Fill in your Azure API key
7. pip install -r backend/requirements.txt                    # IN Commmand prompt

steps:
cd files.../backend 
python -m venv venv
venv\Scripts\activate
pip install -r backend/requirements.txt

8. npm install                                                # IN Commmand prompt
9. Start backend                                              # IN Commmand prompt
python -m uvicorn main:app --reload

10. Start frontend                                            # IN Commmand prompt
npm run dev