import { ADD_INVESTMENT,
    UPDATE_RISK_LEVEL,
    ADD_QUESTION,
    NEXT_QUESTION,
    PREVIOUS_QUESTION,
    SUBMIT_ANSWERS,
    TOGGLE_ANSWER } from '../constants';

export function addInvestment(amount){
    return {
        type: ADD_INVESTMENT,
        payload:{
            investment: amount
        }
    };
}

export function updateRiskLevel(riskLevel) {
    return {
        type: UPDATE_RISK_LEVEL,
        payload: {
            riskLevel: riskLevel
        }
    };
}

export function addQuestion(question, options){
    return {
        type: ADD_QUESTION,
        payload: {
            question: question,
            options: options
        }
    };
}

export function toggleAnswer(answerIndex, questionIndex){
    return {
        type: TOGGLE_ANSWER,
        payload: {
            answer: answerIndex,
            question: questionIndex
        },
    };
}

export function nextQuestion(index){
    return {
        type: NEXT_QUESTION,
        payload: {
            questionNumber: index
        }
    };
}

export function prevQuestion(index){
    return {
        type: PREVIOUS_QUESTION,
        payload: {
            questionNumber: index
        }
    };
}

export function submitAnswer(risk){
    return {
        type: SUBMIT_ANSWERS,
        payload: {
            riskLevel: risk
        }
    };
}
